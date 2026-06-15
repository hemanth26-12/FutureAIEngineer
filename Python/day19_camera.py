class Camera:
    def __init__(self,camera_name,location):
        self.camera_name= camera_name
        self.location= location

cam = Camera("DTS","Hyderabad")

print(cam.camera_name)
print(cam.location)
        