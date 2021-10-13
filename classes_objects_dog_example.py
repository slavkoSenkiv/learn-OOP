class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'My name is {self.get_name()}')

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def sound(self):
        print('my sound is Woof')
        return 'Woof'

    def bite(self, times):
        bites = 'bite ' * times
        print(bites)


def play_obj(class1, bites):
    print('class1', end=' | ')
    class1

    print('class1.sound()', end=' | ')
    class1.sound()

    print('class1.bite(bites)', end=' | ')
    class1.bite(bites)

    print('class1.age |', class1.age)
    print('class1.get_age() |', class1.get_age())

    print('\n')


play_obj(Dog('Bill', 2), 4)
play_obj(Dog('Timm', 3), 5)



