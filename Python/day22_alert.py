class AlertSystem:

    def send_alert(self):
        print("Alert Sent")

class SecurityAlert(AlertSystem):
    pass

alert1 = SecurityAlert()
alert1.send_alert()