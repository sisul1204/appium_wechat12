# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/9 19:18
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '5.1.1',
            'browserName': 'browser',
            'noReset': 'true',
            'deviceName': 'emulator-5554'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        self.driver.find_element_by_id('index-kw').click()
        self.driver.find_element_by_id('index-kw').send_keys('appium')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MobileBy.ID, 'index-bn')))
        self.driver.find_element_by_id('index-bn').click()


