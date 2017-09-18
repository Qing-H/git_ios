
####777777

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
        sleep(5)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        xcall_page = Xcall(self.driver)
        xcall_page.a_login()

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

#   1.A拨打B，B未接听，2.A取消拨打
    def test_2_a_call_b(self):
        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(5)
        result = verify_call(self)
        self.assertTrue(result)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

        xcall_page.a_hangup_4()
        sleep(2)
        result = verify_hangeup(self)
        self.assertTrue(result)

#   1.A拨打B，B拒接
    def test_3_a_call_b(self):
        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(5)
        result = verify_call(self)
        self.assertTrue(result)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

#   1.A拨打B，B接听,2.AB通话中，3.A挂断
    def test_4_a_call_b(self):
        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(5)
        result = verify_call(self)
        self.assertTrue(result)

        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        #sleep(5)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

        xcall_page.a_hangup_2()
        sleep(2)
        result = verify_hangeup(self)
        self.assertTrue(result)

        #print("do something @proc1")
        #print("proc1 t1e rev ***:", self.param.recv())

#   1.A拨打B，B接听，2.AB通话中，3.B挂断
    def test_5_a_call_b(self):
        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(5)
        result = verify_call(self)
        self.assertTrue(result)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        #sleep(5)


        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())
#   1、A、B登录，2、B去后台10S，B返回app，A拨打电话，3、B接通电话
    def test_6_a_call_b(self):

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(2)
        result = verify_call(self)
        self.assertTrue(result)

        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        self.param.recv()
        self.param.send(self.pipe_num)

############## 2、A拨打电话，A去后台，3、B接听，B挂断，4，A返回app，给B拨电话
    def Ctest_7_a_call_b(self):

        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(2)
        result = verify_call(self)
        self.assertTrue(result)


        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        self.driver.background_app(30)

        result = verify_hangeup(self)
        self.assertTrue(result)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

    def ctest_7_a_call_b_2(self):

        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(5)
        result = verify_call(self)
        self.assertTrue(result)

        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

#  1、A、B登录，2、A拨打电话，A去后台(15S)，3、B接听，B去后台，4，A返回app，B返回app
    def ctest_8_a_call_b(self):
        xcall_page = Xcall(self.driver)
        xcall_page.a_call_b()
        sleep(2)
        result = verify_call(self)
        self.assertTrue(result)
        sleep(2)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        self.driver.background_app(15)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())
        result = verify_answer(self)
        self.assertTrue(result)

        self.param.send(self.pipe_num)
        self.param.recv()

    def test_a_logoff(self):
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        xcall_page = Xcall(self.driver)
        xcall_page.a_logoff()
        sleep(3)
        result = verify_xlogoff(self)
        self.assertTrue(result)
        sleep(2)
        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())




    @classmethod
    def tearDownClass(cls):
        sleep(4)
        cls.driver.quit()


if __name__ == '__main__':
    # pipe = 1
    report = "/Users/zoe/Desktop/xcall_ios/xcallTest_Framework_iOS/report" + '/report_xcall_a.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='xconnect_ios', description='报告')
        suite = unittest.TestLoader().loadTestsFromTestCase(A_XcallTests)
        runner.run(suite)
