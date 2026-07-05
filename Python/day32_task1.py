class WeakPasswordError(Exception):
    pass

try:
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")

    if len(Password) < 6:
        raise WeakPasswordError("Password must be at least 6 characters long.")
except WeakPasswordError as e:
    print(e)
else:
    print("Login Successful")