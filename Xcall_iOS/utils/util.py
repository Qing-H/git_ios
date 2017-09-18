import os
from time import sleep
from appium import webdriver
from actions import *
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config
from utils.verify_items import *


def click_buttoni(test_evm, btn_id):
    bt = test_evm.driver.find_element_by_accessibility_id(btn_id)
    bt.click()


def click_wait_buttoni_byclass(test_evm, btn_id):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i<time_interval_times:
        i = i+1
        try:
            bt = test_evm.driver.find_element_by_class_name(btn_id)
        except Exception:
            sleep(time_interval)
            continue
        bt.click()
        break

def click_wait_buttoni(test_evm, btn_id):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_accessibility_id(btn_id)
        except Exception:
            sleep(time_interval)
            continue
        bt.click()
        break


def wait_buttoni(test_evm, btn_id):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_accessibility_id(btn_id)
        except Exception:
            sleep(time_interval)
            continue
        return

def click_send_buttoni(test_evm,btn_id,keys):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_accessibility_id(btn_id)
        except Exception:
            sleep(time_interval)
            continue
        bt.send_keys(keys)
        break


#ios ==> value
def click_wait_buttoni_byname(test_evm, name):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i<time_interval_times:
        i = i+1
        try:
            bt =test_evm.driver.find_element_by_name(name)
        except Exception:
            sleep(time_interval)
            continue
        bt.click()
        break




