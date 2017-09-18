import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config
import BasePage
#driver = webdriver.Remote(BasePage.Base.url, BasePage.Base.desired_caps)

class Conversion(BasePage.Base):
    conversion = "会话"
    friends_name_2 = Config().get('friends_name_2')
    input = "输入信息"
    send = "Send"
    back = "xconnect titlebar back"
    more = "xconnect icon more"
    group_name_1 = Config().get('group_name_1')
    notchoose = "xconnect box notchoose"
    test_group = "测试组"
    group_name_2_1 = Config().get('group_name_2_1')
    start2 = "发起(2)"
    msg_2 = Config().get('msg_2')
    new_group_1= Config().get('new_group_1')
    new_group_2 = Config().get('new_group_2')
    old_group_1 = Config().get('old_group_1')
    old_group_2 = Config().get('old_group_2')
    group = "xconnect titlebar group"
    reduction = "xconnect reduction"
    delete1 = "删除(1)"
    delete = "删除"
    group_name = "群聊名称"
    TypeTextField = "XCUIElementTypeTextField"
    clear = "Clear text"
    save = "保存"
    please_input = "请输入20个字以内"

    def click_conversion(self):
        self.click_wait_button_byacc(self.conversion)

    def click_friend(self):
        self.click_wait_button_byacc(self.friends_name_2)

    def click_send_msg(self,msg):
        self.click_send_byacc(self.input,msg)

    def click_send(self):
        self.click_wait_button_byacc(self.send)

    def click_back(self):
        self.click_wait_button_byacc(self.back)

    def click_more(self):
        self.click_wait_button_byacc(self.more)

    def click_group_name_1(self):
        self.click_wait_button_byacc(self.group_name_1)

    def click_group_name_2_1(self):
        self.click_wait_button_byacc(self.group_name_2_1)

    def click_new_group_1(self):
        self.click_wait_button_byacc(self.new_group_1)

    def click_new_group_2(self):
        self.click_wait_button_byacc(self.new_group_2)

    def click_old_group_1(self):
        self.click_wait_button_byacc(self.old_group_1)

    def click_old_group_2(self):
        self.click_wait_button_byacc(self.old_group_2)

    def click_notchoose_i(self,i):
        self.click_wait_button_byacc_i(self.notchoose,i)

    def click_test_group_i(self,i):
        self.click_wait_button_byacc_i(self.test_group,i)

    def click_start(self):
        self.click_wait_button_byacc(self.start2)

    def click_group(self):
        self.click_wait_button_byacc(self.group)

    def click_group_name(self):
        self.click_wait_button_byacc(self.group_name)

    def click_reduction(self):
        self.click_wait_button_byacc(self.reduction)

    def click_delete1(self):
        self.click_wait_button_byacc(self.delete1)

    def click_delete(self):
        self.click_wait_button_byacc(self.delete)

    def click_TypeTextField(self):
        self.click_wait_button_byclass(self.TypeTextField)

    def click_clear(self):
        self.click_wait_button_byacc(self.clear)

    def click_save(self):
        self.click_wait_button_byacc(self.save)

    def click_send_group_name(self,groupname):
        self.click_send_byacc(self.please_input,groupname)








