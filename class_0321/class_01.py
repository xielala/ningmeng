

#类与对象
#class  命名规范：首字母大写  驼峰命名  见明知意
#类的概念  具有某一类共同属性和特性的失误
#类一般包含属性以及方法

#软件测试工程师类
class TesterEngineer:

    #属性值
    age='25'
    sex='女'
    wages='1w'
    experience='3年'

    #方法/函数
    def function_test(self):
        print("我会做功能测试")

    def api_test(self):
        print("我会做性能测试")

    def perforpence_test(self):
        print("我会做性能测试")

    def safety_test(self):
        print(self.name+"我会做安全测试")

    @classmethod  #类方法
    def coding(cls):
        print("我还会写代码")

    @staticmethod  #静态方法
    def sing():  #这里不用传self  也是普通函数
         print("我还会唱歌")

#创建实例调用
tester=TesterEngineer()
print(tester.age)
tester.api_test()


#不创建实例调用
TesterEngineer().api_test() #类名必须带括号

#类方法的调用   @classmethod
TesterEngineer.coding()#类方法的调用，这里无需加给类加括号
tester.coding() #实例调用类方法

#静态方法调用  @staticmethod
TesterEngineer.sing()
tester.sing()


#1.实例方法self  列方法cls  静态方法（普通方法）  实例和类名都可以直接调用
#2.不同点：静态方法和类方法不能调用类里面的属性值  如果要使用，请自己传递
#3.什么时候去定义为静态方法和类方法   当你的某个函数与其他的类函数没有半毛钱关系的时候
#就可以定位为静态方法或者类方法