class Student:
    def __init__(self,Name,Roll_Number,Branch,Year,filename="Student_System.txt"):
        self.Name = Name
        self.Roll_Number = Roll_Number
        self.Branch = Branch
        self.Year = Year
        self.filename = filename


    def Add_Student(self):
        try:
            with open(self.filename,"a") as f:
                add = f"{self.Name}|{self.Roll_Number}|{self.Branch}|{self.Year}\n"
                f.write(add)
                print(f"Add to {self.filename}.")

        except IOError as e:
            print("ERROR :",e)
        
    def Display_Student(self):
        try:
            with open(self.filename, "r") as f:
                students = f.readlines()
                if not students:
                    print("No students found.")
                else:
                    print("\n--- All Students ---")
                    for student in students:
                        details = student.strip().split("|")
                        if len(details) == 4:
                            print(f"Name: {details[0]}, Roll: {details[1]}, Branch: {details[2]}, Year: {details[3]}")
        except IOError as e:
            print("ERROR :", e)

    def Search_Student(self):
        try:
            search_term = input("Enter Name or Roll Number to search: ")
            with open(self.filename, "r") as f:
                students = f.readlines()
                found = False
                for student in students:
                    details = student.strip().split("|")
                    if len(details) == 4 and (search_term.lower() == details[0].lower() or search_term == details[1]):
                        print(f"\n--- Student Found ---")
                        print(f"Name: {details[0]}, Roll: {details[1]}, Branch: {details[2]}, Year: {details[3]}")
                        found = True
                if not found:
                    print("Student not found.")
        except IOError as e:
            print("ERROR :", e)

    def Delete_Student(self):
        try:
            search_term = input("Enter Name or Roll Number to delete: ")
            with open(self.filename, "r") as f:
                students = f.readlines()
            
            new_students = []
            found = False
            for student in students:
                details = student.strip().split("|")
                if len(details) == 4 and (search_term.lower() == details[0].lower() or search_term == details[1]):
                    found = True
                    print(f"Deleted: {details[0]}")
                else:
                    new_students.append(student)
            
            if found:
                with open(self.filename, "w") as f:
                    f.writelines(new_students)
                print("Student removed successfully.")
            else:
                print("Student not found.")
        except IOError as e:
            print("ERROR :", e)


s = [Student("Hemanth",6624,"CSM","3rd"),
     Student("HEMAN",66222,"CSD","4rd")]
s[1].Add_Student()
s[0].Display_Student()

s[1].Delete_Student()
s[0].Display_Student()
