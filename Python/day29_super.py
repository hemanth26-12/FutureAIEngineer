class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self, name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no
        
        print("Name :",self.name)
        print("Roll :", roll_no)

s1 = Student(name="Hemanth",roll_no=420)