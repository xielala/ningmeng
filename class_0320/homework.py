# -*- coding:utf-8 -*-
# @Time : 2020/3/20 12:30
# @Email : 965917155@qq.com
# @Auther : huanhuan

# for i in range(1,6):
#     print("*"*i)


# 等腰三角形
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end='')
#     for k in range(1,i+1):
#         print("* ",end='')
#     print("")


#99乘法表
# 1*1=1
# 1*2=2 2*2=4
for i in range(1,10):#行数 1 2 3
    for j in range(1,i+1):#行里的第一个数
        print("{0}*{1}={2} ".format(j,i,i*j),end="")
    print("")


#冒泡排序 相邻的两个数比较
a=[1,7,4,89,34,2]