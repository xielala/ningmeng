# -*- coding:utf-8 -*-
# @Time : 2020/3/19 12:27
# @Email : 965917155@qq.com
# @Auther : huanhuan

#异常处理&调试（类与对象再讲调试）
#异常：你在运行代码过程中遇到的任何问题可能会出现的错误   带有error字样的  都是异常
#异常处理：我们对代码中多有可能出现的异常  进行的处理
#疑问：我们为什么要进行处理？

import os
# #1.处理某种错误  2.处理某种异常  3.有错就抓
# try:
#     os.mkdir("python11")#FileExistsError
# # except FileExistsError:#1.捕捉指定异常
# # except Exception:#2.捕捉所有异常
# except:  # 3.同上捕捉所有异常
#     print("这是抓到的异常")
# os.rmdir("python666") #OSError
# print(a)#NameError

# def add(a,b):#TypeError: add() missing 1 required positional argument: 'b'
#     print(a+b)
# add(3)

# file=open("火妹.txt") #io.UnsupportedOperation: not writable
# file.write("hahahhahaaaaa")


#1.既要抓，还有有处罚措施
# try:
#     os.rmdir("python11")
# except OSError as e:#1.捕捉指定异常  存到变量里e
#     print("这是抓到的异常")
#     print("错误为：{0}".format(e))
#     #拿一个小本本机器零
#     file=open("error.txt","a+",encoding='utf-8')
#     file.write(str(e))
#     file.close()






#2.try  except  finally
try:
    os.rmdir("python11")
except Exception as e:#1.捕捉指定异常  存到变量里e
    print("这是抓到的异常")
    print("错误为：{0}".format(e))
    #拿一个小本本机器零
    file=open("error.txt","a+",encoding='utf-8')
    file.write(str(e))
    file.close()
finally:
    print("捕捉或者未捕捉到异常都会执行")





#2.try  except  else
try:
    os.rmdir("python11")
except Exception as e:#1.捕捉指定异常  存到变量里e
    print("这是抓到的异常")
    print("错误为：{0}".format(e))
    #拿一个小本本机器零
    file=open("error.txt","a+",encoding='utf-8')
    file.write(str(e))
    file.close()
else:#跟try下面的代码一起执行，捕捉不到异常的时候执行
    print("捕捉或者未捕捉到异常都会执行")