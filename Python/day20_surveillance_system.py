class SurveillanceSystem:

    def start_system(self):
        print("System Started")

    def detect_person(self):
        print("Person Detected")

    def send_alert(self):
        print("Alert Sent")


system = SurveillanceSystem()

system.start_system()
system.detect_person()
system.send_alert()