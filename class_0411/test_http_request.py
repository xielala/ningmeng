
import unittest
from class_0411.http_request1 import HttpRequest

class TestHttpRequest(unittest.TestCase):

    def __init__(self,url,data,method,methodName):
        super(TestHttpRequest,self).__init__(methodName)
        self.url=url
        self.data=data
        self.method=method

    def setUp(self) -> None:
        print("我要开始测试了")

    def test_login(self):#测试正常的登录
        res=HttpRequest().http_request(self.url,self.data,self.method)
        print("测试请求的结果是：{0}".format(res))

    # def test_err_login(self):#测试错误的登录
    #     # url = 'http://nnn/Login.do'
    #     # data = {"username": "superadmin", "password": "1122222"}
    #     res=HttpRequest().http_request(self.url,self.data,self.method)
    #     print("测试请求的结果是：{0}".format(res))

    def tearDown(self) -> None:
        print("我要结束测试类")


class TestMath(unittest.TestCase):
    def test_add(self):
        print('a+b=',10)

    def test_sub(self):
        print('a+b=', 10)