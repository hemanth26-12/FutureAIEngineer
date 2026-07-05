class InvalidUserError(Exception):
    pass
class WeakPasswordError(Exception):
    pass
class InvalidRoleError(Exception):
    pass

Username = input("Enter your username: ")
Password = input("Enter your password: ")
Role = input("Enter your role : ")

errors = []
if Role not in ["Admin", "Security", "Operator"]:
    errors.append(InvalidRoleError("Invalid role."))
if len(Password) < 8:
    errors.append(WeakPasswordError("Password must be atleast 8 characters long."))
if Username == "":
    errors.append(InvalidUserError("Invalid Username."))

if errors:
    for e in errors:
        print(e)
else:
    print("Access Granted")