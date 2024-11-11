class Singleton:
    _instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if Singleton.init_flag == False:
            return
        print("初始化播放器")
        Singleton.init_flag = True

# 测试
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # 输出: True
print(singleton1)
print(singleton2)