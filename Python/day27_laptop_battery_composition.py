class Battery:
    def __init__(self,capacity):
        self.capacity = capacity   

class Laptop:
    def __init__(self):
        self.battery = Battery("5000mAh")
    def show_battery(self):
        print("Battery Capacity :" , self.battery.capacity)

c1 = Laptop()
c1.show_battery()
