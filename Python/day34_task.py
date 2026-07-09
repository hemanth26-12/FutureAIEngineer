class Employee:
    def __init__(self,Name,ID,Department,Salary,filename="application.txt"):
        self.Name = Name
        self.ID = ID
        self.Department = Department
        self.Salary = Salary
        self.filename = filename
    def display(self):
        print("Name :",self.Name)
        print("ID ",self.ID)
        print("Department ",self.Department)
        print("Salary ", self.Salary)
        print("_"*30)
    def add_employee(self):
        try:
            with open(self.filename,"a+") as f:
                new = f"{self.Name}|{self.ID}|{self.Department}|{self.Salary}\n"
                f.write(new)
                print("Successfully Added.")

        except FileNotFoundError as e:
            print(e)  
    def Display_employee(self):
        try:
            with open(self.filename,"r") as f:
                reads = f.readlines()
                print(reads)

        except FileNotFoundError as e:
            print(e)
      
    def Search_employee(self):
        search = input("Enter the Name to Search: ")
        try:
            with open(self.filename,"r") as f:
                reads = f.readlines()
                found = False
                for read in reads:
                    details = read.strip().split("|")
                    if len(details) == 4 and (search.lower() == details[0].lower() or search== details[1]):
                        print(f"\n--- Employee Found ---")
                        print(f"Name: {details[0]}, ID: {details[1]}, Department: {details[2]}, Salary: {details[3]}")
                        found = True
                if not found :
                    print("NOT FOUND")
        except IOError as e:
            print("ERROR :", e)
e = [Employee("Hemanth","D246","AI",50000),
     Employee("Sai Rohith","D256","ML",35000)
]
for e1 in e:
    e1.add_employee()
    print("-"*30)
    e1.Search_employee()
    e1.display()



