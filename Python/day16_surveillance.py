try:
    file = open("camera_log.txt","r")
    print(file.read())
except:
    print("Camera Log Missing")
