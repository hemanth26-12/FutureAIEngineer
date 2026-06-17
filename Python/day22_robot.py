class Robot:

    def greet(self):
        print("Hello")

class SecurityRobot(Robot):
    pass

r1 = SecurityRobot()
r1.greet()