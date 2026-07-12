class Student:
    def __init__(self,Name,Roll_NO,Marks,Filename = "StudentMarks.txt"):
        self.Name = Name
        self.Roll_No = Roll_NO
        self.Marks = Marks
        self.Filename = Filename

    def display(self):
        print("Name :",self.Name)
        print("Roll No:",self.Roll_No)
        print("Marks :",self.Marks)
    @staticmethod
    def search_Name(student_list, search_name):
        search_name = search_name.strip().lower()
        for s1 in student_list:
            if s1.Name.lower() == search_name:
                return s1
        return None


students =[Student("Hemanth",6624,97),
          Student("Ravi",6625,89),
          Student("Ramu",6626,79)
]
s2 = Student("Ramesh",6634,88)
students.append(s2)

for student in students:
    with open(student.Filename,"a+") as f:
        add = f"{student.Name}  \n Roll No : {student.Roll_No} \n  Marks : {student.Marks}\n"
        f.write(add)

    student.display()
    print("_" * 30)

search_name = input("Enter The Student Name to search: ").strip()
result = Student.search_Name(students, search_name)
if result:
    print("\nStudent found:")
    result.display()
else:
    print("\nStudent not found.")





