class Base1:
    def __init__(self):
        self.name = "Base1"

    def greet(self):
        return f"Hello from {self.name}"

class Base2:
    def __init__(self):
        self.name = "Base2"

    def greet(self):
        return f"Greetings from {self.name}"

class Derived(Base1, Base2):
    def __init__(self):
        # 调用父类的构造函数
        Base1.__init__(self)
        Base2.__init__(self)

    def greet(self):
        # 可以调用父类的方法
        return f"{Base1.greet(self)} and {Base2.greet(self)}"

# 创建派生类的实例
obj = Derived()

# 调用 greet 方法
print(obj.greet())  # 输出: Hello from Base1 and Greetings from Base2

# 检查对象的属性
print(obj.name)  # 输出: Base2 (由于最后调用 Base2 的构造函数)
