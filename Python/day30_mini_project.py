class Laptop :
    def __init__(self,Brand,Model,RAM):
        self.Brand = Brand
        self.Model = Model
        self.RAM = RAM
class Department:
    def __init__(self,Department_Name,Floor_Number):
        self.Department_Name = Department_Name
        self.Floor_Number = Floor_Number
class Employees:
    def __init__(self,EmpName,EmpId,Laptop_object,Department_object):
        self.EmpName = EmpName
        self.EmpId = EmpId
        self.Laptop_object = Laptop_object
        self.Department_object = Department_object
    def display(self):
        print("Employee name :",self.EmpName)
        print("Employee ID :",self.EmpId)
        print("\n")
        print("Laptop Brand :",self.Laptop_object.Brand)
        print("Laptop Model :",self.Laptop_object.Model)
        print("Laptop RAM :",self.Laptop_object.RAM)
        print("\n")
        print("Department Name :",self.Department_object.Department_Name)
        print("Floor Number :",self.Department_object.Floor_Number)
l1 = Laptop(Brand="Dell",Model="XPS 15",RAM="16GB")
d1 = Department(Department_Name="IT Department",Floor_Number="5 Floor")
e1 = Employees(EmpName="HEMANTH",EmpId=420,Laptop_object=l1,Department_object=d1)
e1.display()