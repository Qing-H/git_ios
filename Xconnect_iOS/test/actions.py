from appium.webdriver.common.touch_action import TouchAction

from utils.config import Config
from utils.util import *
import os
from time import sleep
from appium import webdriver
from actions import *
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *

def a_login(test_evm):
    #textfields1 = test_evm.driver.find_element_by_name("请输入账号")
    #textfields2 = test_evm.driver.find_element_by_name("请输入密码")
    phone_num_a = Config().get('phone_num_a')
    password_a = Config().get('password_a')
    click_send_buttoni(test_evm,"请输入账号",phone_num_a)
    click_send_buttoni(test_evm, "请输入密码",password_a)
    #textfields1.send_keys(phone_num_a)
    #textfields2.send_keys(password_a)
    click_wait_buttoni_byclass(test_evm, 'XCUIElementTypeOther')
    click_wait_buttoni_byclass(test_evm, 'XCUIElementTypeButton')


def a_logoff(test_evm):
    click_wait_buttoni(test_evm,"我")
    click_wait_buttoni(test_evm, "登出")

def a_logoff_cancel(test_evm):

    pass

def a_logoff_confirm(test_evm):

    pass

def a_sendmsg(test_evm):
    friends_name_2 = Config().get('friends_name_2')
    click_wait_buttoni(test_evm, "会话")
    click_wait_buttoni(test_evm, friends_name_2)
    input = test_evm.driver.find_element_by_accessibility_id("输入信息")
    msg_1 = Config().get('msg_1')
    input.send_keys(msg_1)
    click_wait_buttoni(test_evm, "Send")
    click_wait_buttoni(test_evm, "Send")
    click_wait_buttoni(test_evm, "xconnect titlebar back")


def a_sendpic(test_evm):
    pass


def a_addfriends1(test_evm):
    click_wait_buttoni(test_evm, "会话")
    click_wait_buttoni(test_evm, "xconnect icon more")
    group_name_1 = Config().get('group_name_1')
    click_wait_buttoni(test_evm, group_name_1)
    click_wait_buttoni(test_evm, "xconnect box notchoose")
    test_evm.driver.find_elements_by_name("测试组")[1].click()
    # click_button(test_evm, "测试组")
    # group_name_2 = Config().get('group_name_2')
    # click_wait_buttoni(test_evm, group_name_2)
    group_name_2_1 = Config().get('group_name_2_1')
    click_wait_buttoni(test_evm, group_name_2_1)
    test_evm.driver.find_elements_by_accessibility_id("xconnect box notchoose")[1].click()
    click_wait_buttoni(test_evm, "发起(2)")
    msg_2 = Config().get('msg_2')
    click_send_buttoni(test_evm, "输入信息", msg_2)
    click_wait_buttoni(test_evm, "Send")
    click_wait_buttoni(test_evm, "Send")
    click_wait_buttoni(test_evm, "xconnect titlebar back")


def a_addfriends2(test_evm):
    pass

def a_deletefriends(test_evm):
    click_wait_buttoni(test_evm, "会话")
    new_group_1 = Config().get('new_group_1')
    click_wait_buttoni(test_evm, new_group_1)  # ’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘
    click_wait_buttoni(test_evm, "xconnect titlebar group")
    click_wait_buttoni(test_evm, "xconnect reduction")
    click_wait_buttoni(test_evm, "xconnect box notchoose")
    click_wait_buttoni(test_evm, "删除(1)")
    click_wait_buttoni(test_evm, "删除")
    click_wait_buttoni(test_evm, "xconnect titlebar back")
    click_wait_buttoni(test_evm, "xconnect titlebar back")

def a_quit(test_evm):
    click_wait_buttoni(test_evm, "会话")
    new_group_1 = Config().get('new_group_1')
    click_wait_buttoni(test_evm, new_group_1)  # ’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘
    click_wait_buttoni(test_evm, "xconnect titlebar group")
    click_wait_buttoni(test_evm, "退出群聊")
    click_wait_buttoni(test_evm, "退出")


def a_rename1(test_evm):
    click_wait_buttoni(test_evm, "会话")
    click_wait_buttoni(test_evm, "xuelei3161、xuelei3162、xuelei3163")  # ’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘
    click_wait_buttoni(test_evm, "xconnect titlebar group")
    click_wait_buttoni(test_evm, "群聊名称")
    click_wait_buttoni_byclass(test_evm, "XCUIElementTypeTextField")
    click_wait_buttoni(test_evm, "Clear text")
    new_group_1 = Config().get('new_group_1')
    click_send_buttoni(test_evm, "请输入20个字以内", new_group_1)
    click_wait_buttoni(test_evm, "保存")
    click_wait_buttoni(test_evm, "xconnect titlebar back")
    click_wait_buttoni(test_evm, "xconnect titlebar back")

def a_rename2(test_evm):
    pass


#长按删除第二个会话
def a_press_delete(test_evm):
    pass
#长按置顶第三个会话
def a_press_stick(test_evm):
    pass

#长按取消置顶
def a_press_unstick(test_evm):
    pass
