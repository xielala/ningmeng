
# 2.输入num为四位数，对其按照如下的规则进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第一位和第四位互换，第二位和第三位呼唤
# 3）最后合起来最为加密后的整数输出

num=input("请输入4位数字") # input 从控制台获取的数据  都是字符串形式
new_num=""
for item in num:
    new_num+=str((int(item)+5)%10)
last_num=new_num[::-1]
print(last_num)