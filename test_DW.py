# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/9 11:02
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['devcieName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print('搜索测试用例')
        '''
        1.打开雪球app
        2.点击搜索输入框
        3.输入阿里巴巴
        4.获取股价，并判断股价>200
        '''

        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"阿里巴巴\"]').click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        print(current_price)
        assert current_price>200


    def test_touchaction(self):
        sleep(4)
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width*0.5)
        y_start = int(height * 0.8)
        y_end = int(height * 0.2)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"阿里巴巴\"]').click()
        current_price = self.driver.find_element_by_xpath('//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        print(current_price)

    def test_myinfo(self):
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('18252063029')
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('a1234567')

        #通过组合方式
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()


        #点击股票
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"阿里巴巴\"]').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("花甲老头").'
                                                        'instance(0));').click()


if __name__ == '__main__':
    pytest.main()
