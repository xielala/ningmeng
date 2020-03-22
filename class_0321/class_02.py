#软件测试工程师类
class TesterEngineer:

    #初始化函数，在java里叫构造函数  这里没有return返回值
    def __init__(self,name,sex='女'):
        self.name=name
        self.sex=sex
        self.height=155


    #属性值
    age='25'
    wages='1w'
    experience='3年'

    #方法/函数
    def coding(self,lines,language='python'):
        print(self.name+"用{0}语言写了{1}行代码".format(language,lines))

    def test(self,*args):
        self.cooking(*args)
        print("我会做性能测试")

    def cooking(self,*args):
        for item in args:
            print("我会做{0}".format(item))

    def play_game(self,game_name):
        self.cooking('火锅')
        return ('我会玩{0}'.format(game_name))

    @classmethod  #类方法
    def function_test(cls):
        print("我还会功能测试")

    @staticmethod  #静态方法
    def sing(music_name):  #这里不用传self  也是普通函数
         print("我还会唱{0}歌".format(music_name))

t=TesterEngineer('花花',18)

#什么时候使用初始化函数
#如果某个属性是多个函数共用的  就可以使用初始化函数
# t.coding(20)
# t.coding(2000,'java')
# t.cooking('青椒炒肉','番茄炒蛋','宫保鸡丁')
# print(t.play_game('王者荣耀'))
# t.sing('稻香')
t.test('豆腐','冬瓜')