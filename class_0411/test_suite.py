

import unittest
from class_0411.test_http_request import TestHttpRequest

#收集用例TestSuite
my_suite=unittest.TestSuite()

#加载用例
#方法一：测试类里的一个实例就是一个测试用例
# url = 'http://nnn/Login.do'
# data_normal = {"username": "superadmin", "password": "111111"}#正常登录的数据
# data_err = {"username": "superadmin", "password": "1122222"}#错误的数据
#数据量大时，把数据存到Excel来读取
test_data=[{"url":'http:/nnn/Login.do',
            'data':{"username": "superadmin", "password": "111111"},
            'method':'get',
            'title':'正常登录'},
           {"url": 'http://nnn/Login.do',
            'data': {"username": "superadmin", "password": "222222"},
            'method': 'get',
            'title':'输入密码错误登录'}
           ]
for item in test_data:
    print("正在执行的用例是：{0}".format(item['title']))
    my_suite.addTest(TestHttpRequest(item['url'], item['data'],item['method'], "test_login"))
# my_suite.addTest(TestHttpRequest(url,data_normal,'get',"test_normal_login"))
# my_suite.addTest(TestHttpRequest(url,data_err,'post',"test_err_login"))

# 方法二--》TestLoader
loader=unittest.TestLoader()#用例加载器
# loadTestsFromTestCase如果你想一次性加载某个测试类里面的所有用例
# my_suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
# 如果你想一次性加载某个模块下的所有用例  如果某个模块下有多个测试类
# from class_0411 import test_http_request
# my_suite.addTest(loader.loadTestsFromModule(test_http_request))

#执行用例
runner=unittest.TextTestRunner()
runner.run(my_suite)