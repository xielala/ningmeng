
# 控制语句  分支分流  循环语句  for  while
# 判断语句  if  elif  else  关键字
# if  条件语句（比较 逻辑 成员 均可）    字符串 列表 元组空数据==False  非空数据==True
# age=20
# if age>18:  # 当if后面的语句满足条  运算结果是True 就会执行下面的子语句
#     print('恭喜你，成年了')


# if 条件语句：
#     子语句
# else:
#     子语句


# if 条件语句：
#     子语句
# elif:
#     子语句
# else:
#     子语句

# input() 函数  从控制台获取一个数据  获取的数据都是字符串类型
age=int(input("请输入你的年龄："))
if age>=18:
    print("恭喜你，成年了")
elif 18>age>=0:
    print("加油长大，小屁孩")
else:
    print("您的年龄输入有误")


# 下节课  预告 for while 嵌套for