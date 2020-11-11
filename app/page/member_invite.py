# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 9:23
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class MemberInvite(BasePage):

    def addmember_by_manual(self):
        from app.page.contact_add import ContactAdd
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, '//*[@text="添加成功"]').text



