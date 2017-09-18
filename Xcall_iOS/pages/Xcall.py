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

class Xcall(BasePage.Base):

    def a_login(self):
        self.click_wait_button_byacc("菜单")
        self.click_wait_button_byacc("0、登录")
        self.click_wait_button_byacc("100000000000006")

    def a_logoff(self):
        self.click_wait_button_byacc("菜单")
        self.click_wait_button_byacc("1、退出")
        self.click_wait_button_byacc("确定")
        #self.click_wait_button_byclass_1("XCUIElementTypeButton")

    def b_login(self):
        self.click_wait_button_byacc("菜单")
        self.click_wait_button_byacc("0、登录")
        self.click_wait_button_byacc("100000000000007")

    def b_logoff(self):
        self.click_wait_button_byacc("菜单")
        self.click_wait_button_byacc("1、退出")
        self.click_wait_button_byacc("确定")


    def a_call_b(self):
        self.click_wait_button_byacc("菜单")
        self.click_wait_button_byacc("2、外呼")
        self.click_wait_button_byclass("XCUIElementTypeTextField")
        #self.click_wait_button_byacc("delete")
        #self.click_wait_button_byacc("delete")
        self.click_send_byname("10000000000000","7")
        self.click_wait_button_byacc("拨打电话")

    def b_answer(self):
        self.click_wait_button_byacc("接听")
#  b未接通，a挂断
    def a_hangup_1(self):
        self.click_wait_button_byacc("主:000006,被:000007 状态:外呼")
        self.click_wait_button_byacc("0、挂断")

#  b接通，a挂断
    def a_hangup_2(self):
        self.click_wait_button_byacc("主:000006,被:000007 状态:通话")
        self.click_wait_button_byacc("0、挂断")

    def a_hangup_3(self):
        self.click_wait_button_byacc("主:000006,被:000007 状态:挂断")
        self.click_wait_button_byacc("0、挂断")

    def a_hangup_4(self):
        self.click_wait_button_byacc("主:000006,被:000007 状态:振铃")
        self.click_wait_button_byacc("0、挂断")

#  b未接通，b挂断
    def b_hangup_1(self):
        self.click_wait_button_byacc("主:000006,被:000007 状态:来电")
        self.click_wait_button_byacc("0、挂断")

#  b接通，b挂断
    def b_hangup_2(self):
        self.click_wait_button_byacc("主:000006,被:000007 状态:通话")
        self.click_wait_button_byacc("0、挂断")

    def find(self):
        self.click_wait_button_byacc("aa")



'''
    def a_login(self):
        self.click_wait_button_byacc("菜单")
        self.click_wait_button_byacc("登录")
        self.click_wait_button_byacc("测试200006")
        self.click_wait_button_byacc("菜单")
'''