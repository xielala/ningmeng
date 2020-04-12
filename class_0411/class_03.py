import requests
class HttpRequest:
    """完成http请求"""

    def __init__(self,url,data):
        self.url=url
        self.data=data

    def get_request(self):#实例方法，只能通过实例来调用
        res=requests.get(self.url,self.data)
        print("返回结果是：",res.json())

    def post_request(self):
        res = requests.post(self.url, self.data)
        print("返回结果是：", res.cookies)


#重写：跟父类的函数名一样叫重写
#拓展：函数名是父类里面没有的就叫拓展
class PythonHttpRequest(HttpRequest):#继承

    def __init__(self,a,b,url,data):#超继承
        super(PythonHttpRequest,self).__init__(url,data) # 调用父类里面的__init__
        self.a=a
        self.b=b

    def print_msg(self):
        self.get_request()#类里面的方法 属性 只能是实例调用
        print("我是一个没有用的函数，我在这里用父类的方法")

    def add(self):
        print("a+b=",self.a+self.b)

#继承的时候  子类要不要传初始化参数  看父类

url='http://nnn/Login.do'
data={"username":"superadmin","password":"111111"}
PythonHttpRequest(1,2,url,data).get_request()


# unittest核心步骤
# unittest中最核心的四个概念是：testcase testsuit testrunner testfixfure
# TestCase：一个testcase的实例就是一个测试用例
#
# TestSuite：多个测试用例集合在一起
#
# TestLoader：加载TestCase到TestSuite中的
#
# TextTestRunner：用来执行测试用例的。其中的run(test)会执行TestSuite/TestCase中的用例 run(test)方法
#
# TextTestResult：保存TextTestRunner执行的测试结果
#
# fixture：测试用例环境的搭建和销毁，测试前准备环境的搭建(setUp)，执行测试代码(run)以及测试后环境的还原(tearDown)


