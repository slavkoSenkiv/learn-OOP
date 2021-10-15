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





