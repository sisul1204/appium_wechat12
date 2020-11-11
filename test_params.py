# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/9 16:37
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


class TestParams:
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


    @pytest.mark.parametrize('searchkey, type,expect_price', [
        ('alibaba', 'BABA', 290),
        ('xiaomi', '01810', 25)
    ])
    def test_search(self, searchkey, type, expect_price):
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        self.driver.find_element_by_id('com.xueqiu.android:id/name').click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert_that(current_price, close_to(expect_price, expect_price*0.1))