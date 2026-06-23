class Alert:
    def __init__(self,alert_id,location,severity):
        self.alert_id = alert_id
        self.location = location
        self.severity = severity

class SecuritySystem:
    def __init__(self):
        self.alert = []

    def add_alert(self,alert):
        self.alert.append(alert)

    def show_alert(self):
        for alert in self.alert:

            print("Alert ID :",alert.alert_id)
            print("Location :",alert.location)
            print("Severity :",alert.severity)
            print("-"*30)

s1 = Alert("AL101","Main Gate","High")
s2 = Alert("AL102","Block-2 Gate","Medium")
s3 = Alert("AL106","Security Room","High")
s4 = Alert("AL108","HQ Room","High")


a1 = SecuritySystem()
a1.add_alert(s1)
a1.add_alert(s2)
a1.add_alert(s3)
a1.add_alert(s4)


a1.show_alert()



