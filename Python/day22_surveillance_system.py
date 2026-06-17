class SurveillanceSystem:

    def start_system(self):
        print("System Started")
    def detect_person(self):
        print("Person Detected")

class SmartSurveillance(SurveillanceSystem):
    def send_alert(self):
        print("Alert Sent")

r1 = SmartSurveillance()
r1.start_system()
r1.detect_person()
r1.send_alert()