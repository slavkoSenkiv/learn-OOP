class Pet:
    def __init__(self, type, name, age, color):
        self.name = name
        self.type = type
        self.age = age
        self.color = color

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old and I'm {self.color}")


class Cat(Pet):
    def __init__(self, type, name, age, color, fur):
        super().__init__(type, name, age, color)
        self.fur = fur

    def speak(self):
        print('Meow')


class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    def speak(self):
        pass

c = Cat('cat', 'Tim', 7, 'black', 'long')
d = Dog('dog', 'Bil', 9, 'brown')


def play_obj(class1):
    print('type', class1.type)
    print('name', class1.name)
    print('age', class1.age)
    print('color', class1.color)
    print('.speak()', end=' '); class1.speak()
    print('.show()', end=' '); class1.show()
    print('\n')


play_obj(c)
play_obj(d)
print(c.fur)

f = Fish('Bubble', 10)
f.show()
f.speak()


# new day new remembering

class Weapon:
    place_in_bag = 2

    def __init__(self, name, weight, hands, attack):
        self.name = name
        self.weight = weight
        self.attack = attack
        self.hands = hands


class Sword(Weapon):

    def physical_damage(self):
        damage_size = self.attack * self.place_in_bag
        return damage_size


class Stuff(Weapon):

    def __init__(self, name, weight, hands, attack, length):
        super().__init__(name, weight, hands, attack)
        self.length = length

    def magical_damage(self):
        damage_size = self.attack * self.place_in_bag * self.length
        return damage_size


sword = Sword('sword', 100, 1, 100)
stuff = Stuff('stuff', 50, 2, 200, 0.3)

print(sword.name, sword.physical_damage())
print(stuff.name, stuff.magical_damage())
