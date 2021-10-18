class Person():
    ppl_num_attr = 0  # static class attributes useful because can be passed with from other files as part of the class

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def ppl_num_attr_meth(cls):
        return cls.ppl_num_attr

    @classmethod
    def add_person(cls):
        cls.ppl_num_attr += 1


p1 = Person('Tim')
p2 = Person('Bil')

print('p1.name', p1.name)
print('p1.ppl_num_attr', p1.ppl_num_attr)
print('p2.name', p2.name)
print('p2.ppl_num_attr', p2.ppl_num_attr)

print('\n')

print('Person.ppl_num_attr', Person.ppl_num_attr)
Person.ppl_num_attr += 1
print('Person.ppl_num_attr', Person.ppl_num_attr)
Person.ppl_num_attr += 1
print('p1.ppl_num_attr', p1.ppl_num_attr)
p1.ppl_num_attr += 1
p2.ppl_num_attr += 1
Person.ppl_num_attr += 1
print('Person.ppl_num_attr', Person.ppl_num_attr)
