
s='hello!'
# 字符串的去除默认指定字符 字符串.strip(指定字符)


# 字符串拼接 + 用加号拼接是要保证变量值类型要一直
s_1='python11,'
s_2='中秋节快乐！'
s_3=666 # 整数
print(s_1+s_2+str(s_3))
print(s_1+s_2,s_3)


# 字符串格式化输出  %format
age=18
name='小行星'
score=99.99
print('python11期的{0}，今年{1}岁'.format(name,age))

# 格式化输出2:%  %s字符串,也可以是任何数据   %d只能数字、整形、浮点数  %f浮点数
print('python11期的%s，今年%d岁，考试%.2f分'%(name,age,score))

# 下节课：列表  元组  字典 运算符
# 下下节课：条件 循环