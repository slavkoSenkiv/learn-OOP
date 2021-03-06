class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade + 100  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avarage_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course('Math', 2)
course.add_student(s1)
course.add_student(s2)

print('course.add_student(s3)', course.add_student(s3))
print('course.students', course.students)
print('course.get_avarage_grade()', course.get_avarage_grade())
print('s1.get_grade()', s1.get_grade())
print('s1.grade', s1.grade)


