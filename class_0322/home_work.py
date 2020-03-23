
# debug-->出错的时候  哪行代码出错，就debug打在哪一行
# 超继承  用法na'hang以及什么时候用

class MathMethod:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return "我是父类的方法",self.a-self.b

class MathMethod_1(MathMethod):
    def divide(self):
        return self.a/self.b

    def add(self):#重写
        super(MathMethod_1,self).add()  #超继承 :想用父类的方法，又不想重新写
        print("我是子类的方法",self.a+self.b+10)


MathMethod_1(5,6).add()