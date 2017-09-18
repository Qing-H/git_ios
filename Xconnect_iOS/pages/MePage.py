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

class Me(BasePage.Base):
    account = "请输入账号"
    password = "请输入密码"
    TypeOther = 'XCUIElementTypeOther'
    TypeButton = 'XCUIElementTypeButton'
    me = "我"
    off = "登出"
    phone_num_a = Config().get('phone_num_a')
    password_a = Config().get('password_a')

    def click_me(self):
        self.click_wait_button_byacc(self.me)

    def click_send_account(self):
        self.click_send_byacc(self.account,self.phone_num_a)

    def click_send_password(self):
        self.click_send_byacc(self.password,self.password_a)

    def click_TypeOther(self):
        self.click_wait_button_byclass(self.TypeOther)

    def click_TypeButton(self):
        self.click_wait_button_byclass(self.TypeButton)

    def click_off(self):
        self.click_wait_button_byacc(self.off)

