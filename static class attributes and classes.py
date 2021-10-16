class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people_()

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person('Tim')
p2 = Person('Jil')

Person.number_of_people = 8
print(p1.number_of_people)
Person.number_of_people = 9
print(p2.number_of_people)
print(Person.add_person())
