class Person:
    def __init__(self,name):
        self.name = name
class EmployeeID(Person):
    def __init__(self, name,EmpID):
        super().__init__(name)
        self.EmpID = EmpID
class SecuirtyOfficer(EmployeeID):
    def __init__(self,name,EmpID,Area):
        super().__init__(name,EmpID)
        self.Area = Area

class ChiefSecurityOfficer(SecuirtyOfficer):
    def __init__(self, name, EmpID, Area,Level):
        super().__init__(name, EmpID, Area)
        self.Level = Level

        print("Name :",self.name)
        print("Employee ID :",self.EmpID)
        print("Area :",self.Area)
        print("Clearance Level :",Level)
        print("-"*30)

c1 = ChiefSecurityOfficer(name="Hemanth",EmpID="GH26",Area="Hyerabad",Level="HR")
c1 = ChiefSecurityOfficer(name="Ravi",EmpID="GH24",Area="Hyerabad",Level="DEVELOPER")