import os
from time import sleep
from appium import webdriver
from actions import *
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config
from pages.ConversionPage import Conversion


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class A_iOSTests(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        path = Config().get('path')
        desired_caps = {}
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '10.3'
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['app'] = PATH(
            path
        )
        desired_caps['noReset'] = True
        desired_caps['bundleId'] = "com.ctrip.xplan.ctripxconnect"
        desired_caps['udid'] = "7bf03dd3bed6d6c6826919e8de7632e641186357"
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_a_send_msg(self):
        msg_1 = Config().get('msg_1')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversion()
        conversion_page.click_friend()
        conversion_page.click_send_msg(msg_1)
        conversion_page.click_send()
        conversion_page.click_send()
        conversion_page.click_back()


    def test_b_add_friend1(self):
        msg_2 = Config().get('msg_2')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversion()
        conversion_page.click_more()
        conversion_page.click_group_name_1()
        conversion_page.click_notchoose_i(0)
        conversion_page.click_test_group_i(1)
        conversion_page.click_group_name_2_1()
        conversion_page.click_notchoose_i(1)
        conversion_page.click_start()
        conversion_page.click_send_msg(msg_2)
        conversion_page.click_send()
        conversion_page.click_send()
        conversion_page.click_back()

    def test_c_rename(self):
        new_group_1 = Config().get('new_group_1')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversion()
        conversion_page.click_old_group_1()
        conversion_page.click_group()
        conversion_page.click_group_name()
        conversion_page.click_TypeTextField()
        conversion_page.click_clear()
        conversion_page.click_send_group_name(new_group_1)
        conversion_page.click_save()
        conversion_page.click_back()
        conversion_page.click_back()

    def test_d_delete_friend(self):
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversion()
        conversion_page.click_new_group_1()
        conversion_page.click_group()
        conversion_page.click_reduction()
        conversion_page.click_notchoose_i(0)
        conversion_page.click_delete1()
        conversion_page.click_delete()
        conversion_page.click_back()
        conversion_page.click_back()



    def ctest_m_logoff_confirm(self):
        pass



    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.driver.quit()

'''
if __name__ == '__main__':
    # pipe = 1
    report = "/Users/zoe/Desktop/Test_Framework_iOS/report" + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='xconnect_ios', description='报告')
        suite = unittest.TestLoader().loadTestsFromTestCase(A_iOSTests)
        # unittest.TextTestRunner(verbosity=2).run(suite)
        # runner.run(TestBaiDu('test_search'))
        runner.run(suite)
'''