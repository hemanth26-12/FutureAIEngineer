class Robot:
    def speak(self):
        print("I am a robot")
class AI_Robot(Robot):
    def speak(self):
        print("I am an AI Robot")

r1 = AI_Robot()
r1.speak()