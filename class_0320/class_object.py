

#python  类的语法  关键字class   def 函数名(参数)：函数的关键字
#class 类名：类名的规范是  数字字母下划线组成  不能以数字开头  首字母大小写  驼峰命名
    #类属性
    #类方法

class BoyFriend:
    #类属性
    height=175
    weight=130
    money="500万"

    #类函数/类方法
    def cooking(self):
        print("男朋友要会做饭")

    def earn(self):
        print("男朋友要月薪3万")

    def print_self(self):
        print(self)




#实例   对象  具体的一个例子  类名()
bf=BoyFriend()  #这是创建一个实例
print(bf)  #打印实例本身
bf.print_self()  #打印实例本身，同上

#实例具有类里面的所有属性和方法的使用权限
#调用属性  实例.属性名
#调用方法  实例.方法名()


