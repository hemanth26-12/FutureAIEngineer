class User:
    def permissions(self):
        print("Basic Permissions")

class SecurityOfficer(User):
    def permissions(self):
        print("Monitor Cameras")

class Administrator(User):
    def permissions(self):
        print("Full Control")

users = [
    User(),
    SecurityOfficer(),
    Administrator()
]

for user in users:
    print(f"{user.__class__.__name__}:", end=" ")
    user.permissions()