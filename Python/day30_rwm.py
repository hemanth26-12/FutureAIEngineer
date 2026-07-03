class Camera:
    def __init__(self,name):
        self.name = name
    def record(self):
        print("Recording...")
class Microphone:
    def __init__(self,name):
        self.name = name
    def listen(self):
        print("Listening...")
class MotionSensor:
    def __init__(self,name):
        self.name = name
    def detect_motion(self):
        print("Detecting motion...")
class AISurveillance(Camera, Microphone, MotionSensor):
    def __init__(self, name):
        Camera.__init__(self, name)
        Microphone.__init__(self, name)
        MotionSensor.__init__(self, name)
    def display(self):
        print("Surveillance System Name:", self.name)
        self.record()
        self.listen()
        self.detect_motion()
c1 = AISurveillance(name="Hemanth")
c1.display()