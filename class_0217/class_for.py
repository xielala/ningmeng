
# 循环 for while  官架子
# python  for 循环语法：
# for item in 某个数据类型（字符串 列表 元组 字典 集合等）：
# in ? 成员运算符号  in   not in
# for循环的循环次数  由数据的元素个数决定
# s='hello'
# l=[1,2,3]
# d={1:'111',2:'ddd'}
# for item in d:  # 遍历s里的元素  然后赋值给item
#     print(item,d[item])

# L=[5,6,9,3,7]
# m=0
# for s in L:
#     m=m+s
# print(m)


# range函数  生成整数序列
# range(m,n,k) m头默认为0，n尾，k步长默认1，取头不取尾巴
# for item in range(3):  # 0 1 2
#     print("循环次数")

# L=[5,6,9,3,7]
# # 请利用for循环  根据L的索引值，打印出每个元素的值
# for item in range(len(L)):
#     print(L[item])

# 请利用for循环和range函数  完成1-100整数相加和（包含1和100）
# sum=0
# for i in range(1,101):
#     sum+=i
# print("所有值的和:{0}".format(sum))


#嵌套循环
# 请把嵌套循环里面的每个值打印出来
# L=[["monica","生生","小黄"],["hellen","keai","宝贝"]]
# for i in L: #每次循环都到一个子列表  赋值给i
#     for j in i:
#         print(j)

# 请利用嵌套for循环生成一个直角三角形
# *
# **
# ***
# ****
# *****
for i in range(6):
    print("*"*i)