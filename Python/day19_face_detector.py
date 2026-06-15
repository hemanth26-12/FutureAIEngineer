class FaceDetector:
    def __init__(self,model_name,accuracy):
        self.model = model_name
        self.accurancy = accuracy

face = FaceDetector("CVV",80.00)

print(face.model)
print(face.accurancy)
        