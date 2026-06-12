try:
    user = int(input("Enter the Experience:"))
    print("user year experience:",user)
except NameError,ValueError:
    print("Invalid Experience Value")