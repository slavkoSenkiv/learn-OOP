
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)

    def get_name(self):
        return self.name

    def bite_more(self, x):
        return x + 1

    def bark(self):
        print('woof')

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


print('d1', end=' ')
d1 = Dog('Tim', 32)

print('d1.name', end=' ')
print(d1.name)

print('d1.get_name()', end=' ')
print(d1.get_name())

print('d1.get_age()', end=' ')
print(d1.get_age())

print('d1.set_age(17)', end=' ')
d1.set_age(17)

print('d1.get_age()', end=' ')
print(d1.get_age())

print(d1.bite_more(2))

"""
d2 = Dog('Bill', 12)
print(d2.name)
print(d2.get_name())
print(d2.get_age())
"""

"""
classes
class Dog: 
there can be millions of dogs but Dog class describe each of them

methods
def bark(self):
    print('woof')
methods are actions that can be done within a class,they are functions by nature

parameters
(self) in bark method is method's parameter, there can be a lot of them
self param. unlike others possible params says that method will be conducted on the called object itself

def __init__ ():
if the class has __init__ method, the  method is automatically called when the object of this class is called

def __init__(self, name, age):
    self.name = name
    self.age = age
    print(name)
it also can store class attributes
"""





