import os
from time import sleep
from appium import webdriver
from actions import *
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config
from pages.MePage import Me


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

    def test_b_login(self):
        me_page = Me(self.driver)
        me_page.click_send_account()
        me_page.click_send_password()
        me_page.click_TypeOther()
        me_page.click_TypeButton()


    def test_a_logoff(self):
        me_page = Me(self.driver)
        me_page.click_me()
        me_page.click_off()



    def ctest_m_logoff_confirm(self):
        pass



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

'''
if __name__ == '__main__':
    # pipe = 1
    report = "/Users/zoe/Desktop/Test_Framework_iOS/report" + '/report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='xconnect_ios', description='报告')
        suite = unittest.TestLoader().loadTestsFromTestCase(A_iOSTests)
        runner.run(suite)
'''