import unittest
import HTMLTestRunner
from class_0406.class_request1 import TestHttp



test_data=[{'url':'http://www.baidu.com','data':{'mobile':15677777777},'excepted':'这是预期结果','method':'get'},
           {'url':'http://www.baidu.com','data':{'mobile':15677777777},'excepted':'这是预期结果','method':'get'},
           {'url':'http://www.baidu.com','data':{'mobile':15677777777},'excepted':'这是预期结果','method':'get'},
           {'url':'http://www.baidu.com','data':{'mobile':15677777777},'excepted':'这是预期结果','method':'get'}]

suite=unittest.TestSuite()#存储用例
for item in test_data:
    suite.addTest(TestHttp('test_api',item['url'],item['data'],item['excepted'],item['method']))



# 新鲜 html
with open('test.test_report.html','wb') as  file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=1, title="python learn", description='测试报告')
    runner.run(suite)
