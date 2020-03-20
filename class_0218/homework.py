

# 设计一个登录程序，不同的用户名和密码存在字典里
# 输入用户名，如果用户名不存在或者为空，则一直提示请输入用户名
# 如果用户名正确，提示请输入密码，如果密码跟用户名不对应，则提示密码错误
# 如果密码输入错误超过3次，中断程序运行
# 当密码错误时，提示还有几次机会
# 当用户名和密码都输入成功的时候，提示登录成功

user={"admin":"111111","user":"000000"}

username=input("请输入用户名：")
while username not in user:
    print("用户名错误")
    username = input("请输入用户名：")

password=input("请输入密码：")
times=3
while password != user[username]:
    times-=1
    print("您还有{0}次机会".format(times))
    if times==0:
        password = input("登录失败！")
        break
    password = input("密码错误，请重新输入：")
if password == user[username]:
    print("登录成功")