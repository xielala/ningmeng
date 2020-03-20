
# python内置函数
# print input len type str int float list
# pop append insert keys split replace strip
# remove clear

# 总结一下函数的特点：
# 可以重复使用
# 函数名明明的规范：小写字母分开  不能以数字开头  不同的字母之间用下划线隔开
# 函数的语法：def 关键字
# def 函数名(参数1，参数2，参数3):
#     函数体：你希望这个函数去给你实现什么功能
# def da_lao(name="花花"): # 形参/未知参数   默认参数
#     print("{0}是大佬".format(name))
# # 调用：函数名()
# da_lao()
# da_lao("测试")



def add_nums(m,n,k=1):
    sum = 0
    for i in range(m,n):
        sum=sum+i
    print("求和值:",sum)

sum(1,101)