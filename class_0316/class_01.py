# -*- coding:utf-8 -*-
# @Time : 2020/3/17 12:37
# @Email : 965917155@qq.com
# @Auther : huanhuan


#相对路径  绝对路径

#疑问：如果我们要打开操作一个文件  使用绝对路径好  还是相对路径好：都可以

import os

#新建一个目录/新建一个文件加
# os.mkdir("Huanhuan")

#跨级新建目录  用/符号来代表路径下的不同层级
# 必须确保上面的层级是存在的
# os.mkdir("Huanhuan/vict")  #相对路径

# os.mkdir("D:\\测试路径")  #为什么用两个\\  因为一个\一般是转移字符  也可以用一个/


#删除   删除文件也是一级一级的删除
# os.mkdir("Huanhuan")
# os.rmdir("Huanhuan")


#拓展一：Python  可否强制删除
#拓展二：怎么去新建文件 open 删除文件？







import os

# 路径的获取1   获取当前工作目录
# path1=os.getcwd()
# print("1路径：{0}".format(path1))
#
# # 路径的获取2   获取当前文件的绝对路径
# path2=os.path.realpath(__file__)
# print("2路径：{0}".format(path2))
#
#
# #第三个知识点：如何拼接路径
# new_path_1=os.getcwd()+"\\python11"
# print(new_path_1)
# os.mkdir(new_path_1)


# join
# new_path_2=os.path.join(os.getcwd(),"python666","sub_1")
# print(new_path_2)
# os.mkdir(new_path_2)


#判断是文件还是目录
# print(os.path.isfile(os.getcwd())) #返回值  布尔值
# print(os.path.isdir(os.getcwd())) #返回值  布尔值


#怎么判断文件是否存在
# print(os.path.exists(os.path.realpath(__file__)))

# 罗列出当前路径的所有文件夹
print(os.listdir(os.getcwd()))

