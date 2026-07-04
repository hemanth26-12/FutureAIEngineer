from abc import ABC,abstractmethod

class Robot(ABC):
    @abstractmethod
    def perform_task(self):
        pass
class SecurityRobot(Robot):
    def perform_task(self):
        print("Monitoring Area")

class MedicalRobot(Robot):
    def perform_task(self):
        print("Assisting Doctors")

s = SecurityRobot()
s.perform_task()
m = MedicalRobot()
m.perform_task()
