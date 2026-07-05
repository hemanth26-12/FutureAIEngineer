from abc import ABC, abstractmethod
class Machine(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def perform_task(self):
        pass
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
class WeldingRobot(Machine):
    def __init__(self, name, model):
        super().__init__(name, model)
    def start(self):
        pass
    def stop(self):
        pass
    def perform_task(self):
        pass
class PaintingRobot(Machine):
    def __init__(self, name, model):
        super().__init__(name, model)
    def start(self):
        pass
    def stop(self):
        pass
    def perform_task(self):
        pass
class AssemblyRobot(Machine):
    def __init__(self, name, model):
        super().__init__(name, model)
    def start(self):
        pass
    def stop(self):
        pass
    def perform_task(self):
        pass
items = [
    WeldingRobot("WeldMaster 3000", "WM-3000"), 
    PaintingRobot("PaintPro 2000", "PP-2000"),
    AssemblyRobot("AssemBot 1000", "AB-1000")
]
for item in items:
    item.display_info()
    print()
