class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students_num = max_students
        self.students_enrolled = []

    def add_student(self, student):
        if len(self.students_enrolled) < self.max_students_num:
            self.students_enrolled.append(student)
        else:
            print('too much students inside course already')
            return False

    def get_average_grade(self):
        value = 0
        for student in self.students_enrolled:
            student_grade = student.grade
            value += student_grade
        average_grade = value / len(self.students_enrolled)
        return average_grade


def play_student(name1, age1, grade1):
    s = Student(name1, age1, grade1)
    # print(s.name)
    # print(s.age)
    # print(s.grade)
    # print('\n')
    return s


s1 = play_student('Tim', 20, 50)
s2 = play_student('Bill', 21, 60)

c = Course('Math', 2)
print(c.name)
print(c.max_students_num)
print(c.students_enrolled)
c.add_student(play_student('Tim', 20, 50))
print(c.students_enrolled)
c.add_student(s1)
print(c.students_enrolled)
c.add_student(s2)
print(c.students_enrolled)
print(c.get_average_grade())

