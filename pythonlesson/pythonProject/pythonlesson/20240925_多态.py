# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement this method")
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# # 使用多态
# shapes = [Rectangle(5, 10), Circle(7)]
#
# for shape in shapes:
#     print(f"Area: {shape.area()}")
class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s在愉快的玩耍"%self.name)

class XiaoTianDog(Dog):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s飞到天上去玩耍" %self.name)
class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s和%s在愉快的玩耍" %(self.name,dog.name))

# wangcai = Dog("旺财")
wangcai = XiaoTianDog("旺财")
xiaoming = Person("小明")
wangcai.game()
xiaoming.game_with_dog(wangcai)