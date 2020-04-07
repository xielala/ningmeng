
import unittest,requests
from API_AUTO.tools.http_request import HttpRequest
from class_0406.get_data import GetData



class TestHttp(unittest.TestCase):

    def __init__(self,methodName,url,data,excepted,method):
        super(TestHttp,self).__init__(methodName) #超继承 保留父类的__init__
        self.url=url
        self.data=data
        self.excepted=excepted
        self.method=method

    def test_api(self):

            res=HttpRequest().http_request(self.url,self.data,self.method)
            if res.cookies: #如果cookie有值，就更新cookie
                setattr(GetData,'Cookie',res.cookies)
            try:
                self.assertEqual(self.excepted,res.json()['code'])
            except AssertionError as e:
                print('测试出错了：'.format(e))
                raise e
            print(res.json())

