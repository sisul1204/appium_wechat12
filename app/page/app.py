# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 9:14
from appium import webdriver

from app.page.base_page import BasePage
from app.page.main import Main


class App(BasePage):

    def start(self):
        if self._driver == None:
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
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(60)
        return self


    def restart(self):
        pass


    def stop(self):
        pass


    def main(self) -> Main:
        return Main(self._driver)