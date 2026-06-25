class Employee:
    def access(self):
        print("General Access")

class Admin(Employee):
    def access(self):
        print("Full System Access")

users = [
    Employee(),
    Employee(),
    Admin(),
    Admin()
]

for user in users:
    print(f"{user.__class__.__name__}:", end=" ")
    user.access()
