class Room:
    def __init__(self,room):
        self.room=room

class House:
    def __init__(self,house):
        self.house = Room(input())
    def show_room(self):
        print("Room Name:",self.house.room)

h1 = House("Living Room")
h1.show_room()
