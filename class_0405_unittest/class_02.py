

import unittest
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

# 执行
runner=unittest.TextTestRunner()
runner.run(suite)

