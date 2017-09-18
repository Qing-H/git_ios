import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config
from utils.config import Config
import BasePage


class xcall(BasePage.Base):
    conversion = "会话"
    friends_name_2 = Config().get('friends_name_2')
    input = "输入信息"
    send = "Send"
    def a_login(test_evm):
        pass



def a_logoff(test_evm):
    click_wait_buttoni(test_evm,"我")
    click_wait_buttoni(test_evm, "登出")

def a_logoff_cancel(test_evm):

    pass

def a_logoff_confirm(test_evm):

    pass



def a_sendpic(test_evm):
    pass



def a_addfriends2(test_evm):
    pass





