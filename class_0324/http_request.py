
# python
#requests第三方库
import requests

# get请求
url='http://www.baidu.com'
res=requests.get(url)#返回一个消息实体
print(res)
print("响应头:",res.headers)
print("响应的状态码：",res.status_code)
print("响应正文：",res.text)


# post请求
url='http://www.baidu.com'
data={'mobilephone':'15638506666'}
print("响应头:",res.headers)
print("响应的状态码：",res.status_code)
print("响应正文：",res.text,type(res.text)) #json   str
print("响应正文2:",res.json(),type(res.json()))#dict  #推荐使用这种
print("cookie",res.cookies)  #类字典形式  key取值
print("cookie",res.cookies['JESSIONID'])

#html  xml  json  -->text
#html  xml  json  -->json()会报错！只有json类型的返回才支持json



#充值
recharge_url='http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':'18688773467','amount':'1000'}
header={"User-Agent":"Mozilla/5.0"}  #这个是伪装的
# 为啥要伪装，服务器识别处理会拒绝  反爬虫  改下user-agent
recharge_res=requests.get(recharge_url,recharge_data,cookies=res.cookies,headers=header)
print("充值结果：",recharge_res)
print("user-argunt",recharge_res.request.headers)

print("代理User-Agent",recharge_res.request.headers) # 获取请求头一定要带
#图片 短信  验证码怎么办？
#1：屏蔽他
#2.万能的
#3.数据库查实时的
#4.手动填