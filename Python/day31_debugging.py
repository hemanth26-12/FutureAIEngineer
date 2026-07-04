from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bus(Vehicle):
    def start_engine(self):
        pass

b = Bus()


"""the program fail due to the abstract
method start_engine() not being implemented in 
Bus class. the bus class inherited the abstract class
vehicle and it is mandatory to implement the 
abstract method start_engine() in bus class. 
else it thows an typeerror.to fix it, implement 
the start_engine() method in the Bus class."""