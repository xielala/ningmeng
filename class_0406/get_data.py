

class GetData:
    Cookie=None

if __name__ == '__main__':
    setattr(GetData, 'Cookie', '小黄')  # 可以直接把类里面的属性值做修改
    print(hasattr(GetData, 'Cookie'))
    print(getattr(GetData, 'Cookie'))
    delattr(GetData, 'Cookie')