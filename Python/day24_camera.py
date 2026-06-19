class Camera:
    def show_location(self,location):
        self.__location = location
        print("Camera Location:",self.__location)

e1 = Camera()
e1.show_location("Main Gate")
