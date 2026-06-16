class Surveillance_System:
    def start_system(self,location):
        print(location)

    def detect_person(self,name):
        print("Person Detected:",name)

    def send_alert(self,alert_type):
        print("Alert Sent:",alert_type)


system = Surveillance_System()

system.start_system("System Started at Main Gate")
system.detect_person("Hemanth")
system.send_alert("Unauthorized Access")
