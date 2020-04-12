



import requests
class HttpRequest:
    """利用request封装get请求和post请求"""

    def http_request(self,url,data,method,cookie=None):
        """
        :return:
        url:请求的地址  http://xxx:port
        data:传递的参数  非必填参数  字典的格式传递参数
        method:请求的方法
        """
        # url = 'http://www.baidu.com'
        # data = {'mobilephone': '15638506666'}
        if method.lower()=="get":
            res = requests.get(url, data=data, cookies=None)
        else:
            res = requests.post(url, data=data,cookies=None)
            # print("响应正文：",res.json())
            return res


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    data = {'mobilephone': '15638506666'}
    res=HttpRequest.http_request(url,data,'post')
    print('登录结果是：',res.json())


    #充值
    recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    recharge_data = {'mobilephone': '18688773467', 'amount': '1000'}
    recharge_res=HttpRequest.http_request(recharge_url,recharge_data,'get',res.cookies)
    print("充值结果是:",recharge_res.json())
# # post请求
# print("响应头:",res.headers)
# print("响应的状态码：",res.status_code)
# print("响应正文：",res.text,type(res.text)) #json   str
# print("响应正文2:",res.json(),type(res.json()))#dict  #推荐使用这种
# print("cookie",res.cookies)  #类字典形式  key取值
# print("cookie",res.cookies['JESSIONID'])

#充值
# recharge_url='http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
# recharge_data={'mobilephone':'18688773467','amount':'1000'}
# header={"User-Agent":"Mozilla/5.0"}  #这个是伪装的
# # 为啥要伪装，服务器识别处理会拒绝  反爬虫  改下user-agent
# recharge_res=requests.get(recharge_url,recharge_data,cookies=res.cookies,headers=header)
# print("充值结果：",recharge_res)
# print("user-argunt",recharge_res.request.headers)

# 练习题：自己结合fiddler+课堂派  抓取课堂派的登录和查询接口
# 获取到考勤的数据
# https   resquests.get(url,data,verify=False)
