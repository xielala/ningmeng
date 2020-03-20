
# 字典  dict 符号{}  大括号 花括号
#1：字典可以存在空a={}
#2：字典里面数据存储方式  key:value
#3：字典里面可以包含任何类型的数据
#4：

a={"class":"python11",
   "student":119,
   "teacher":"girl",
   "age":20,
   "score":[66,77.88,90]}


# 字典取值：字典[key]
print(a["score"][-1])

# 删除 pop(key)

# 新增 a[新key]=value  字典里面存在的key
a["name"]="缓缓"
print(a)

# 修改  a[已存在的key]=新value  字典里面已经镩子的key
a['student']=111
print(a)
