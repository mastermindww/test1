class Animal():
    def eat(self):
        print("eat")

class Cat(Animal):
    def drink(self):
        print("drink")

tom = Cat()
tom.eat()
tom.drink()
