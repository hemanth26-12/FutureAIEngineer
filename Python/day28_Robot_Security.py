class Robot:
    def speak(self):
        print("Robot Speaking")

class SecurityRobot(Robot):
    def speak(self):
        print("Security Alert")



security_robot = SecurityRobot()
security_robot.speak()