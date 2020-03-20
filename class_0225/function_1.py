


# return  当你调用函数的时候，就会饭会一个值  return后面的表达式
# return  在函数里相当于一个结束符号  表示函数到此为止
# 后面的代码不会被执行


# def add_two(a,b):
#     return (a+b)
#     print("我不会被打印出来")
#
# add_two


# 写函数，检查传入列表的长度，如果大于2，
# 那么仅保留前两个长度的内容，并将新内容饭会

# def check_list(list1):
#     if len(list)>2:
#         new_list=list1[0:2]
#     return new_list



# 动态参数  不定长参数   *args   arguments
# def make_sandwich(a,b,c,d):
#     print("您的三明治包含了{0}、{1}、{2}、{3}".format(a,b,c,d))
# make_sandwich("生菜","鸡蛋","培根","牛肉")

# def make_sandwich(*args):
#     all=""
#     for item in args:
#         all+=item
#         all+="、"
#     print("您的三明治包含了："+all)
# make_sandwich("生菜","鸡蛋","培根","牛肉")




# 关键字参数  key-value   **kwargs   key word  必须加**
# def kw_functiion(**kwargs):
#     print(kwargs)
# kw_functiion(x=1,y=2)


def add_all_num(a,*L,**kwargs):
    sum=0
    for item in L:
        sum+=item
    print("和为：",sum)
    print("a的值：",a)
    print("kwargs的值",kwargs)

add_all_num(1,2,3,4,5,6,x=1,y=2)
