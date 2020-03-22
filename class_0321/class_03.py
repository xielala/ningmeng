
#继承
class RobotOne:#第一代机器人
    def __init__(self,name,year=None):
        self.year=year
        self.name=name

    def walking_on_ground(self):
        print(self.name+"只能在平地上行走，有障碍物就会摔倒")

    def robot_info(self):
        print("{0}年生产的机器人{1}，是中国研发的".format(self.year,self.name))


class RootTwo(RobotOne):#第二代机器人继承与第一代机器人

    def __init__(self,name):
        self.name = name

    def walking_on_ground(self): #子类的函数名与父类的函数名一致时，就叫重写
        print(self.name+"可以在平地上平稳的行走")

    def walking_avoid_block(self):  #父类没有，子类有的函数，这里叫拓展
        #我想在子类里面去调用父类的一个函数
        self.robot_info()
        print(self.name+"可以避开障碍物")




#第二代机器人
#集成的类  是否要用到初始化函数  请看是否从弗雷里面继承了
#1.父类有的，我都可以直接拿来用
#2.父类有，子类也有重名的函数，那么子类的实例就优先调用子类的函数
# r2=RootTwo("1990","小王")
# r2.robot_info()
# r2.walking_on_ground()
# r2.walking_avoid_block()


#多继承:继承多个父类
# 第三代机器人
class RootThree(RootTwo,RobotOne):#第三代机器人继承与第一代机器人和第二代机器人
    def jump(self):
        print(self.name+"可以单膝跳跃")

r3=RootThree("大王")
r3.jump()
r3.walking_on_ground()
#具有两个父类的属性和防范  如果两个父类具有同名的方法，优先执行继承的第一个父类里的方法
r3.robot_info()
#疑问：没有传递year参数  调用robot_year就会报错怎么办？
# 自己写的时候注意点，或者重写