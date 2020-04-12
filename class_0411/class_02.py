
import requests
class HttpRequest:
    """完成http请求"""

    def __init__(self,url,data):
        self.url=url
        self.data=data

    def get_request(self):#实例方法，只能通过实例来调用
        res=requests.get(self.url,self.data)
        print("返回结果是：",res.json())

    def post_request(self,url,data):
        res = requests.post(url, data)
        print("返回结果是：", res.cookies)

    @classmethod  #不能使用类里面的初始化参数
    def add(cls):
        print("我是类方法")
        return 10

    @staticmethod #不能使用类里面的初始化参数
    def print_msg():
        print("我是静态方法")

#类方法和静态方法-->可以直接类名.方法名调用
HttpRequest.add()
HttpRequest.print_msg()

#实例方法-->必须创建实例来调用
url='http://nnn/Login.do'
data={"username":"superadmin","password":"111111"}
HttpRequest(url,data).get_request()