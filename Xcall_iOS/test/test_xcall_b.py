
####小白

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
class B_XcallTests(ParametrizedTestCase):
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
        #desired_caps['udid'] = "7bf03dd3bed6d6c6826919e8de7632e641186357"
        desired_caps['udid'] = "7e885bc9ccd6ee1ae4297fc7505f9d48aada496f"
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps["wdaLocalPort"] = "8002"
        cls.driver = webdriver.Remote('http://localhost:4743/wd/hub', desired_caps)
        cls.pipe_num = 2

    def test_1_b_login(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")
        xcall_page = Xcall(self.driver)
        xcall_page.b_login()
        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def test_2_b(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        result = verify_be_called(self)
        self.assertTrue(result)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def test_3_b(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        xcall_page = Xcall(self.driver)
        xcall_page.b_hangup_1()
        sleep(2)
        result = verify_hangeup(self)
        self.assertTrue(result)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def test_4_b(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")
        xcall_page = Xcall(self.driver)
        result = verify_be_called(self)
        self.assertTrue(result)

        xcall_page.b_answer()
        sleep(2)
        result = verify_answer(self)
        self.assertTrue(result)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def test_5_b(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")
        xcall_page = Xcall(self.driver)
        result = verify_be_called(self)
        self.assertTrue(result)

        xcall_page.b_answer()
        sleep(2)
        result = verify_answer(self)
        self.assertTrue(result)

        xcall_page.b_hangup_2()
        sleep(1)
        result = verify_hangeup(self)
        self.assertTrue(result)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
#
    def test_6_b(self):
        xcall_page = Xcall(self.driver)
        self.driver.background_app(10)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        result = verify_be_called(self)
        self.assertTrue(result)

        xcall_page.b_answer()
        result = verify_answer(self)
        self.assertTrue(result)
        xcall_page.b_hangup_2()
        sleep(2)

        self.param.send(self.pipe_num)
        self.param.recv()


    def Ctest_7_b(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        xcall_page = Xcall(self.driver)
        result = verify_be_called(self)
        self.assertTrue(result)

        xcall_page.b_answer()
        result = verify_answer(self)
        self.assertTrue(result)
        sleep(5)

        xcall_page.b_hangup_2()
        result = verify_hangeup(self)
        self.assertTrue(result)

        sleep(30)
        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def ctest_7_b_2(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")
        xcall_page = Xcall(self.driver)
        xcall_page.b_answer()
        sleep(2)
        result = verify_answer(self)
        self.assertTrue(result)
        xcall_page.b_hangup_2()
        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def ctest_8_b(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        xcall_page = Xcall(self.driver)
        xcall_page.b_answer()
        sleep(5)
        result = verify_answer(self)
        self.assertTrue(result)
        self.driver.background_app(15)
        sleep(2)
        result = verify_answer(self)
        self.assertTrue(result)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        self.param.recv()
        self.param.send(self.pipe_num)

    def test_b_logoff(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")
        xcall_page = Xcall(self.driver)
        xcall_page.b_logoff()
        sleep(2)
        result = verify_xlogoff(self)
        self.assertTrue(result)
        sleep(2)
        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)


    @classmethod
    def tearDownClass(cls):
        sleep(4)
        cls.driver.quit()


if __name__ == '__main__':
    # pipe = 1
    report = "/Users/zoe/Desktop/xcall_ios/xcallTest_Framework_iOS/report" + '/report_xcall_b.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='xconnect_ios', description='报告')
        suite = unittest.TestLoader().loadTestsFromTestCase(B_XcallTests)
        runner.run(suite)
