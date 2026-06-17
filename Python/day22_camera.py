class Camera:

    def start(self):
        print("Camera Started")


class AICamera(Camera):
    pass

camera1 = AICamera()
camera1.start()