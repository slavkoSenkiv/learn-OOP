class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name, age)

    def bark(self):
        print('woof')

    def bite_more(self, bites_num):
        return 'bite ' * bites_num

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

class Cat:

    def __init__(self, name):
        self.name = name
        self.nicks = []

    def get_name(self):
        return self.name

    def set_nick(self, nick):
        self.nicks.append(nick)

# <editor-fold desc="print dog part">
d1 = Dog('Tim', 32)
print('d1 = Dog("Tim", 32) | ', d1)

d2 = Dog('Bill', 12)
print('d2 = Dog("Bill", 12) | ', d2)

print('d1.name | ', d1.name)

print('d1.get_name() | ', d1.get_name())

print('d1.get_age() | ', d1.get_age())

print('d1.set_age(17) | ', d1.set_age(17))

print('d1.get_age() | ', d1.get_age())

print('d1.bite_more(2) | ', d1.bite_more(2))
# </editor-fold>
print('\n')
# <editor-fold desc="print dog part">
c1 = Cat('Vin')
print('c1 = Cat("Vin") | ', c1)
print('c1.get_name() | ', c1.get_name())
print('c1.name | ', c1.name)
print('c1.get_name() | ', c1.nicks)
print('c1.set_nick() | ', c1.set_nick('zhyr'))
print('c1.get_name() | ', c1.nicks)
print('c1.set_nick() | ', c1.set_nick('salo'))
print('c1.get_name() | ', c1.nicks)

# </editor-fold>






