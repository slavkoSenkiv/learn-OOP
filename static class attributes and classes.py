class Person():
    ppl_num = 0

    def __init__(self, name):
        self.name = name


p1 = Person('Tim')
p2 = Person('Bil')

print('p1.name', p1.name)
print('p1.ppl_num', p1.ppl_num)  # 0
print('p2.name', p2.name)
print('p2.ppl_num', p2.ppl_num)  # 0

print('\n')

print('Person.ppl_num', Person.ppl_num)  # 0
Person.ppl_num += 1
print('Person.ppl_num', Person.ppl_num)  # 1
Person.ppl_num += 1
print('p1.ppl_num', p1.ppl_num)  # 2
p1.ppl_num += 1
p2.ppl_num += 1
Person.ppl_num += 1
print('Person.ppl_num', Person.ppl_num)  # 3
