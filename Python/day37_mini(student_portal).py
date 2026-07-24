import json
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {"name": self.name, "age": self.age, "grade": self.grade}
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["grade"])
class StudentPortal:
    def __init__(self, filename="students.json"):
        self.students = []
        self.filename = filename

    def add_student(self):
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        while True:
            try:
                age = int(input("Enter student age: ").strip())
                break
            except ValueError:
                print("Age must be a number.")

        grade = input("Enter student grade: ").strip()
        student = Student(name, age, grade)
        self.students.append(student)
        print(f"Student '{name}' added successfully.")
    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        print("\nStudent List:")
        for index, student in enumerate(self.students, start=1):
            print(f"{index}. Name: {student.name} | Age: {student.age} | Grade: {student.grade}")
    def search_student(self):
        keyword = input("Enter student name to search: ").strip().lower()
        if not keyword:
            print("Search term cannot be empty.")
            return
        found = [student for student in self.students if keyword in student.name.lower()]
        if not found:
            print("No matching student found.")
            return
        print("\nSearch Results:")
        for student in found:
            print(f"Name: {student.name} | Age: {student.age} | Grade: {student.grade}")
    def save_to_json(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([student.to_dict() for student in self.students], file, indent=2)
            print(f"Students saved to {self.filename}.")
        except Exception as error:
            print(f"Error saving data: {error}")
    def load_from_json(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.students = [Student.from_dict(item) for item in data]
            print(f"Students loaded from {self.filename}.")
        except FileNotFoundError:
            print("No saved file found.")
        except json.JSONDecodeError:
            print("Invalid JSON file.")
        except Exception as error:
            print(f"Error loading data: {error}")
    def show_menu(self):
        while True:
            print("\nStudent Information Portal")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Save JSON")
            print("5. Load JSON")
            print("6. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.save_to_json()
            elif choice == "5":
                self.load_from_json()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    portal = StudentPortal()
    portal.show_menu()


