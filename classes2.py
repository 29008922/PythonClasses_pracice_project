#!/usr/bin/python3
class students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0...100

    def get_grade(self):
        return self.grade

class course:
    def __init__(self, name, student_max):
        self.name = name
        self.student_max = student_max
        self.student = []

    def add_student(self, student):
        if len(self.student) < self.student_max:
            self.student.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.student:
            value += student.get_grade()
        return value / len(self.student)

A1 = students('Ann Muringe', 17, 95)
A2 = students('Javis Mbugwa', 17, 76)
A3 = students('Robai Nangila', 18, 80)

course = course('Chemistry', 2)
course.add_student(A1)
course.add_student(A2)
course.add_student(A3)

print(course.get_average_grade())
