# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/10 21:55
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker


class TestContact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['devcieName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['newCommandTimeout'] = 60000
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(30)
        self.faker = Faker(locale='zh_CN')

    def teardown(self):
        self.driver.quit()


    def test_addcontact(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys(self.faker.name())
        self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(self.faker.phone_number())
        self.driver.find_element(MobileBy.XPATH,'//*[@text="邮箱　"]/..//*[contains(@class,"EditText")]')\
                                .send_keys(self.faker.email())
        self.driver.find_element(MobileBy.XPATH, '//*[@text="地址"]/..//*[@class="android.widget.LinearLayout"]').click()
        address = self.faker.address()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "请输入")]').send_keys(address)
        self.driver.find_element(MobileBy.XPATH, f'//*[@text="{address}"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        result = self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]').text
        assert "添加成功" == result


        sleep(5)
