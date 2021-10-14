class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


class Cat(Pet):
    def __init__(self, name, age, color, fur):
        super().__init__(name, age, color)
        self.fur = fur

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old and I'm {self.color}")

    def speak(self):
        print('Meow')


class Dog(Pet):
    def speak(self):
        print('Bark')


c = Cat('Tim', 7, 'black', 'long')
d = Dog('Bill', 9, 'brown')


def play_obj(class1):
    print(class1.name)
    print(class1.age)
    print(class1.color)
    class1.speak()
    print('\n')


play_obj(c)
play_obj(d)

print(c.fur)

<<<<<<< Updated upstream
=======
c = Cat('Bill', 34, 'black')  # , 'black')
c.show()
c.speak()
>>>>>>> Stashed changes


