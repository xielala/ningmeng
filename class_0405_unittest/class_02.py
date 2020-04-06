

import unittest
import HTMLTestRunner
# from class_0405_unittest.class_01 import TestMathMethod

suite=unittest.TestSuite()#存储用例
# 方法一：
# 值执行一条  两个整数相加
# suite.addTest(TestMathMethod('test_add_two_positive'))
# suite.addTest(TestMathMethod('test_add_two_negative'))

# 方法二：TestLoader
loader=unittest.TestLoader()#创建一个加载器
#从测试类里面去找
# suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))
#从测试模块里去找
from class_0405_unittest import class_01 #具体到模块
suite.addTest(loader.loadTestsFromModule(class_01))

# # 执行   上下文管理器  --原始的
# with open('test.txt','w+', encoding='utf-8') as file:
#     runner=unittest.TextTestRunner(stream=file, verbosity=2)  #0 1 2  2是最详细的
#     runner.run(suite)
# print(file.close())


# 新鲜 html
with open('test.test_report.html','wb') as  file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=1, title="python learn", description='测试报告')
    runner.run(suite)
