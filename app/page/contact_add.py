# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 9:26
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class ContactAdd(BasePage):


    def input_name(self):
        self.find(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys('xxxx')
        return self

    def set_gender(self):
        self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_phonenum(self):
        self.find(MobileBy.XPATH, '//*[@text="手机号"]').send_keys('18252061235')
        return self


    def click_save(self):
        from app.page.member_invite import MemberInvite
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()
        return MemberInvite(self._driver)
