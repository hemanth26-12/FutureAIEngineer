class Camera:
    def record(self):
        print("Recording...")
class AI:
    def detect(self):
        print("Human Detected")

class Smart(Camera,AI):
    pass

obj=Smart()
obj.record()
obj.detect()

""" the problem was at AI class that 
you have giveninherited from 
Camera class and then again inherited from the
Smart class.so, the solution is to remove the 
Camera class from AI class and then inherit 
both classes in Smart class."""