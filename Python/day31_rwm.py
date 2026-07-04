from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_service(self):
        pass

class Bus(Vehicle):
    def start_service(self):
        print("Bus service started")

class Metro(Vehicle):
    def start_service(self):

        print("Metro service started")

class Flight(Vehicle):
    def start_service(self):
        print("Flight service started")

b = Bus()
b.start_service()

m = Metro()
m.start_service()

f = Flight()
f.start_service()
