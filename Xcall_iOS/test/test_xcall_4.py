######1、A、B登录，2、A拨打电话，A去后台，3、B接听，B挂断，4，A返回app，给B拨电话

import unittest
import multiprocessing
import time

from test_xcall_4_1 import *
from test_xcall_4_2 import *
from utils.parametic import *


class TestOne(ParametrizedTestCase):
    def test_a(self):
        i = 1
        print("proc1 send***: %s" % (i))
        self.param.send(i)
        time.sleep(5)
        print("do something @proc1")
        print("proc1 rev ***:", self.param.recv())


class TestTwo(ParametrizedTestCase):
    def test_b(self):
        i = 2
        print("proc2 rev ---:", self.param.recv())
        print("do something @proc2")
        time.sleep(1)
        print("proc2 send---: %s" % (i))
        self.param.send(i)

def a_test(pipe):
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(A_XcallTests, param=pipe))
    unittest.TextTestRunner(verbosity=2).run(suite)

def b_test(pipe):
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(B_XcallTests, param=pipe))
    unittest.TextTestRunner(verbosity=2).run(suite)
'''
if __name__ == "__main__":
        pipe = multiprocessing.Pipe()
        p1 = multiprocessing.Process(target=a_test, args=(pipe[0],))
        p2 = multiprocessing.Process(target=b_test, args=(pipe[1],))

        p1.start()
        p2.start()

        p1.join(65)
        p2.join(65)

'''
if __name__ == "__main__":
    i = 1
    max_times = 100
    while i<=max_times:
        print("Start running test" + str(i) +"---------------------x1")
        pipe = multiprocessing.Pipe()
        p1 = multiprocessing.Process(target=a_test, args=(pipe[0],))
        p2 = multiprocessing.Process(target=b_test, args=(pipe[1],))

        p1.start()
        p2.start()

        p1.join(65)
        p2.join(65)

        i = i+1
