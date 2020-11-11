# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/10 9:40
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWebView:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '5.1.1',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'deviceName': 'emulator-5554',
            'noReset': 'true',
            'chromedriverExcutable': 'D:\chromedriver'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_webview(self):
        #点击交易
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        sleep(10)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'A股开户').click()

