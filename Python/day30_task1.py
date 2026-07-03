class Camera:
    def record(self):
        print("Recording...")
class AIProcessor:
    def detect(self):
        print("Human Detected...")
class SmartCamera(Camera, AIProcessor):
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Camera Name:", self.name)
        self.record()
        self.detect()

c1 = SmartCamera(name="Hemanth")
c1.display()