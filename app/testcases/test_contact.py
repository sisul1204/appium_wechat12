# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 9:35
from time import sleep

from app.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        sleep(5)
        invitePage = self.main.goto_addresslist().add_member().addmember_by_manual()\
            .input_name().set_gender().input_phonenum().click_save()
        assert '成功' in  invitePage.get_toast()


    def teardown(self):
        pass