class Surveillance:
    def monitor(self):
        print("Monitoring area")
class AISurveillance(Surveillance):
    def monitor(self):
        print("AI Monitoring Area")
        

    def alert(self):
        print("Intruder Detected!")


s1 = AISurveillance()
s1.monitor()
s1.alert()