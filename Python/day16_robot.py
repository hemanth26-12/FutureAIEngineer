try:
    robot = int(input("Enter Robot_ID:"))
    print(robot)
except NameError,ValueError:
         print("Invalid Robot ID")
