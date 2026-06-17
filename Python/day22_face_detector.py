class Detector:

    def detect(self):
        print("Face Detected")

class FaceDetector(Detector):
    pass

detector1 = FaceDetector()
detector1.detect()