class Person:
    population = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")  # 使用类方法创建实例

    @classmethod
    def get_population(cls):
        return cls.population

# 使用类方法创建实例
anonymous_person = Person.create_anonymous()
print(anonymous_person.name)  # 输出: Anonymous

# 获取当前人口
print(f"Current population: {Person.get_population()}")  # 输出: Current population: 1
