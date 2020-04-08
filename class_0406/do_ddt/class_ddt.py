

# ddt ddt+unittest来惊醒数据的处理  第三方库
# 装饰器  可以自行了解  会在你的函数运行之前运行

import unittest
from ddt import ddt,data,unpack

test_data=[[1,3],[2,4,5]]
test_data1=[{'name':'缓缓','age':18},{'name':'lala','age':19}]

@ddt#装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data) #1.装饰测试方法  拿到几个数据，就执行几次方法2.这里必须带*，因为不定长参数是元组，不加的话就认为列表只有一个数据
    @unpack #以逗号拆分参数  如果参数少于5个，推荐该装饰器
    def test_print_data(self,a=None,b=None,c=None):
        print('a:',a)
        print('b:',b)
        print('c:',c)

    @data(*test_data1)
    @unpack #如果要对字典使用该装饰器，参数名必须和参数的key一致
    def test_print_data1(self,name,age):
        print('name:',name)
        print('age:',age)


if __name__ == '__main__':
    TestMath().test_print_data()
    TestMath().test_print_data1()


# 作业
# 1.ddt和unittest的结合使用
# 2.总结：两种unittest+excel 1）超继承 2）ddt
# 3.配置文件的作用