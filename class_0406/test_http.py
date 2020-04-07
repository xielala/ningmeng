


import unittest
from class_0405_unittest.math_method import MathMethod
from class_0406.get_data import GetData
from API_AUTO.tools.http_request import HttpRequest


class TestMathMethod(unittest.TestCase):

    def setUp(self): #
        print("我要开始执行用例了")

    def tearDown(self):
        print('已经执行完毕用例')


    def test_add_two_positive(self):
        global COOKIE
        data={'mobile':11111111,'pwd':123456}
        res=HttpRequest().http_request(self,login_url,data,'get')
        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)

    def test_add_two_zero(self):
        data = {'mobile': 11111111, 'pwd': 123456}
        res = HttpRequest().http_request(self, login_url, data, 'post',getattr(GetData,'Cookie'))
        try:
            self.assertEqual(1, res,'两个0相加出错了')
        except AssertionError as e:
            print("出错了，断言错误是:",e)
            raise e


    def test_add_two_negative(self): #两个复数相加 -1+-2
        res=MathMethod(-1,-2).add()
        print("-1+-2的结果值是：",res)
        try:
            self.assertEqual(-3, res)
        except AssertionError as e:
            print("出错了，断言错误是:",e)
            raise e  # 异常处理完要抛出来，不然用例执行失败也会显示成功



if __name__ == '__main__':
    unittest.main()


#1.全局变量  局部变量 如果要修改全局变量的值 怎么修改
#缺点是关联性比较强  一步错 步步错

#2.反射 --不强调
#缺点是关联性比较强  一步错 步步错

#3.setUp
#缺点是关联性比较强  一步错 步步错