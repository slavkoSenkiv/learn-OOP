class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)

    def get_name(self):
        return self.name

    def add_one(self, x):
        return x + 1

    def bark(self):
        print('woof')

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d1 = Dog('Tim', 32)
print(d1.name)
print(d1.get_name())
print(d1.get_age())
d1.set_age(17)
print(d1.get_age())

"""
d = Dog()
d.bark()
print(d.add_one(5))
print(type(d))

d2 = Dog('Bill', 12)
print(d2.name)
print(d2.get_name())
print(d2.get_age())
"""



