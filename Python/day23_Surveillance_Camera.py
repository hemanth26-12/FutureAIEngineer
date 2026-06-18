class Camera:
    def detect(self):
        print("Object Detected")
class SmartCamera(Camera):
    def detect(self):
        print("Face Detected")
        super().detect()
c1 = SmartCamera()
c1.detect()