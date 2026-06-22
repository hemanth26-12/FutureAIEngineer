class Student:
    def __init__(self,student_name):
        self.student_name = student_name
class College:
    def __init__(self,college):
        self.college = college

clg = College("ACE Engineering")
student = Student("Hemanth")
clg = College(student)

print(clg.college.student_name)
