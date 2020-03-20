

# 运算符  5大类

# 算术运算符  + -  *  /  %
# 模运算  取余运算  判断某个数是偶数还是奇数
# 复制运算符 = += -=

# 比较运算符 >  >=  <   <=   !=  ==   6种比较关系
# 比较结果返回的值是布尔值  True  False
a=10
b=5
print(a>b)
print('get'.upper()=='GET')

# 逻辑运算符 or  and  拓展：not
# 逻辑运算结果饭会的值是布尔值  True  False
print(a>11 and b>4)


# 成员运算符  in    not in
# 返回值也是布尔值
s='hello'
print('l' in s)
l=[1,2,3]
print(1 in l)
d={a:1,b:2,c:3}
print(a in d) # 根据key值判读
