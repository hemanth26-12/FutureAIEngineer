class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Department:", self.department)
        print("Salary:", self.salary)

employees = []
e1 = Employee("Hemanth", 101, "AI", 25000)
e2 = Employee("Rahul", 102, "Cyber Security", 28000)


employees.append(e1)
employees.append(e2)

for employee in employees:
    employee.display()
    print("-" * 30)

# Save employees to file
filename = "application.txt"
with open(filename, "a+") as f:
    for emp in employees:
        line = f"{emp.name}|{emp.emp_id}|{emp.department}|{emp.salary}\n"
        f.write(line)

print(f"Saved {len(employees)} employees to {filename}.")