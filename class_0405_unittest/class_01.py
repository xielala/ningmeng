

#接口测试的本质  就是测试类里面的函数  通过数据驱动
#单元测试的本质  测试函数  代码级别  通过代码级别
#单元测试的框架  unittest+接口  pytest+web-->接口
#pytest+jenkins+allure

#功能测试
# 写用例  TestCase
# 执行用例  1.TestSuit  存储用例  2.TestLoader  找用例，加载用例，存到1.TestSuit
# 对比实际结果 期望结果 判定是否通过  断言 Assert
# 出具测试报告   TextTestRunner

import unittest
from class_0405_unittest.math_method import MathMethod

#写一个测试类  对我们自己写的math  method模块里面的类  进行单元测试
class TestMathMethod(unittest.TestCase):#继承了unittest 里面的TestCase  专门来写用例
    #编写测试用例
    #1.一个用例是一个函数  不能传参  只有self关键字
    #2.所有的用例 （所有的函数  都是test开头  test_）
    def test_add_two_positive(self): #两个正数相加 1+1
        res=MathMethod(1,1).add()
        print("1+1的结果值是：",res)

    def test_add_two_zero(self): #两个0相加 0+0
        res=MathMethod(0,0).add()
        print("0+0的结果值是：",res)

    def test_add_two_negative(self): #两个复数相加 -1+-2
        res=MathMethod(-1,-2).add()
        print("-1+-2的结果值是：",res)

if __name__ == '__main__':
    unittest.main()

#执行顺序是根据用例名的排序:ASCII   也就是abcdefg...
# test_add_two_positive   2
# test_add_two_zero   3
# test_add_two_negative   1


class TestMulti(unittest.TestCase):#继承了unittest 里面的TestCase  专门来写用例
    #编写测试用例
    #1.一个用例是一个函数  不能传参  只有self关键字
    #2.所有的用例 （所有的函数  都是test开头  test_）
    def test_multi_two_positive(self): #两个正数相乘 1*1
        res=MathMethod(1,1).multi()
        print("1+1的结果值是：",res)
        # 加一个断言：判断期望值与实际值对比结果  一致就算测试通过  不一致就测试不通过
        self.assertEqual()

    def test_multi_two_zero(self): #两个0相乘 0*0
        res=MathMethod(0,0).multi()
        print("0+0的结果值是：",res)

    def test_multi_two_negative(self): #两个复数相乘 -1*-2
        res=MathMethod(-1,-2).multi()
        print("-1+-2的结果值是：",res)

if __name__ == '__main__':
    unittest.main()