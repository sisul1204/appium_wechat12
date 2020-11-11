# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 9:20
from app.page.base_page import BasePage
from app.page.member_invite import MemberInvite


class AddressList(BasePage):


    def add_member(self):
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        return MemberInvite(self._driver)
