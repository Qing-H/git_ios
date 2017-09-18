import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
#from utils.util import *
#from utils.verify_items import *
from utils.config import Config
from pages.MePage import Me
from appium.webdriver.common.touch_action import TouchAction
from BasePage import Base
from test_2_ConversionPage import *
from test_1_MePage import *

test_path = "/Users/zoe/Desktop/Test_Framework_iOS/test"
report_path = "/Users/zoe/Desktop/Test_Framework_iOS/report" + "/appium_report.html"
def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_path,pattern="test_*.py")
    for test_suite in discover:
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit

suite = creat_suite()
f = open(report_path,"wb")
runner = HTMLTestRunner(f, verbosity=2, title='Xconnect Test Report', description='测试报告')
runner.run(suite)
f.close()

# report = "D:\study\Test_Framework\\report" + '\\report.html'
# with open(report, 'wb') as f:
#     runner = HTMLTestRunner(f, verbosity=2, title='Xconnect Test Report', description='测试报告')
#     suite1 = unittest.TestLoader().loadTestsFromTestCase(A_ConversionPageTests)
#     suite2 = unittest.TestLoader().loadTestsFromTestCase(A_MePageTests)
#     runner.run(suite1)
#     runner.run(suite2)