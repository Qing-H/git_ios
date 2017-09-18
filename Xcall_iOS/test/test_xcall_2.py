####777777
####  1、A(200006)手机登录，2、给B(200007)拨电话，B未接通，A挂断，反复操作100次
import os
from time import sleep
from appium import webdriver
from actions import *
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config
from pages.Xcall import Xcall


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class A_XcallTests(ParametrizedTestCase):
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
        desired_caps['bundleId'] = "com.ctrip.xplan.xcall"
        desired_caps['udid'] = "7bf03dd3bed6d6c6826919e8de7632e641186357"
        #desired_caps['udid'] = "7e885bc9ccd6ee1ae4297fc7505f9d48aada496f"
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps["wdaLocalPort"] = "8001"
        cls.driver = webdriver.Remote('http://localhost:4733/wd/hub', desired_caps)
        cls.pipe_num = 1

    def test_1_a_login(self):


        xcall_page = Xcall(self.driver)
        xcall_page.a_login()

    def test_2_a_call_b_100(self):

        print("Start running test" + str(0) + "---------------------x1")
        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(5)
        result = verify_call(self)
        self.assertTrue(result)

        xcall_page.a_hangup_1()
        sleep(2)
        result = verify_hangeup(self)
        self.assertTrue(result)
        for i in range(100):
            print("Start running test" + str(i+1) + "---------------------x1")
            xcall_page = Xcall(self.driver)
            xcall_page.a_call_b()
            sleep(5)
            result = verify_call(self)
            self.assertTrue(result)

            xcall_page.a_hangup_3()
            sleep(2)
            result = verify_hangeup(self)
            self.assertTrue(result)



    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.driver.quit()


if __name__ == '__main__':

    suite_a = unittest.TestLoader().loadTestsFromTestCase(A_XcallTests)
    unittest.TextTestRunner(verbosity=2).run(suite_a)