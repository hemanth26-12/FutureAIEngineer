class Camera:
    def __init__(self,name,location,status):
        self.name = name
        self.location = location
        self.status = status

class SurveillanceSystem:

    def __init__(self):
        self.cameras = []
    def add_camera(self,camera):
        self.cameras.append(camera)
    def show_cameras(self):
         
        for camera in self.cameras:

            print("Camera Name :", camera.name)
            print("Location :", camera.location)
            print("Status :", camera.status)
            print("-"*30)

c1 = Camera("Gate Camera", "Main Gate", "Active")
c2 = Camera("Parking Camera", "Parking Area", "Active")
c3 = Camera("Server Camera", "Server Room", "Active")
c4 = Camera("Reception Camera", "Reception", "Inactive") 

system = SurveillanceSystem()
system.add_camera(c1)
system.add_camera(c2)
system.add_camera(c3)
system.add_camera(c4)

system.show_cameras()