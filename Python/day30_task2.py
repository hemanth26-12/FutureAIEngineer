class Person:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print("Name :",self.name)

class Employee():
    def __init__(self,EmpID):
        self.EmpID = EmpID
    def show_ID(self):
        print("Employee ID :",self.EmpID)

class Manager(Person,Employee):
    def __init__(self,name,EmpID,Area):
        Person.__init__(self,name)
        Employee.__init__(self,EmpID)
        self.Area = Area
    def show_Area(self):
        print("Area :",self.Area)

c1 = Manager(name="Hemanth",EmpID="GH24",Area="Hyerabad")
c1.show_name()
c1.show_ID()
c1.show_Area()