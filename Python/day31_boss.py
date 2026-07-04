from abc import ABC, abstractmethod
class HospitalDevice(ABC):
    @abstractmethod
    def operate(self):
        pass
    def __init__(self, ID, Department, Status, Operation):
        self.ID = ID
        self.Department = Department
        self.Status = Status
        self.Operation = Operation
    def display_info(self):
        print(f"ID: {self.ID}")
        print(f"Department: {self.Department}")
        print(f"Status: {self.Status}")
        print(f"Operation: {self.Operation}")
class HeartMonitor(HospitalDevice):
    def __init__(self, ID, Department, Status, Operation):
        super().__init__(ID, Department, Status, Operation)
    def operate(self):
        pass
class Ventilator(HospitalDevice):
    def __init__(self, ID, Department, Status, Operation):
        super().__init__(ID, Department, Status, Operation)
    def operate(self):
        pass
class XRayMachine(HospitalDevice):
    def __init__(self, ID, Department, Status, Operation):
        super().__init__(ID, Department, Status, Operation)
    def operate(self):
        pass
devices = [
    XRayMachine(101, "Radiology", "Operational", "X-Ray Imaging"),
    Ventilator(102, "ICU", "Operational", "Respiratory Support"),
    HeartMonitor(103, "Cardiology", "Operational", "Heart Monitoring")
]
for device in devices:
    device.display_info()
    print()

