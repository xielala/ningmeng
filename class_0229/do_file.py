
#r w a
#r+ w+ a+
#read write append
#rb rb+ wb wb+ ab ab+ 做单元测试的时候
# file=open("python11.txt","r+",encoding='utf-8')
# file.write('哈哈')
# res=file.read()
#res=file.readlines()#读取多行 返回列表
# print(res)


#1：file文件open之后默认是r  只读模式  如果你要写入内容  报错
#2：r+  可读可写  先写的话  从头开始覆盖写  读光标之后的内容  读写跟着光标走
#3：如果要写入中文  要注意编码格式
#4：w 只写  硬要去读就会报错io.UnsupportedOperation: not readable
#5：可读可写  不管是w  还是w+  如果文件存在   就直接清空  再重写
#如果文件不存在  就创建一个文件写
# file=open("python11.txt","w+",encoding='utf-8')
# file.write('哈哈阿斯顿发斯蒂芬阿斯顿发')
# res=file.read()
# print(res)
#6：a 追加  推荐
file=open("python11.txt","a",encoding='utf-8')
file.write('这是追加内容')
#如果文件存在   就追加写   如果文件不存在  就创建一个文件写
file=open("python12.txt","a",encoding='utf-8')
file.write('\n这是追加内容')
file.writelines([777,888])

