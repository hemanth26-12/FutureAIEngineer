class Employee:
    def __init__(self,name,emp_id,access_level):
        self.name = name
        self.emp_id = emp_id
        self.access_level = access_level

    def details(self):
        print("Employee Name :",self.name)
        print("Employee ID :",self.emp_id)
        print("Access Level:",self.access_level)
        print("--"*30)

employee = Employee("daru","Emp33","developer")
employee2 = Employee("Hemanth","Emp420","Admin")
employee3 = Employee("Rahul","Emp421","Manager")

employees = [employee,employee2,employee3]
    

for employeee1 in employees:
    employeee1.details()






        
        