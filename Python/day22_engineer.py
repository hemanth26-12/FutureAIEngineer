class Engineer:
    def show_role(self):
        print("AI Engineer")

class SeniorEngineer(Engineer):
    pass

e1 = SeniorEngineer()
e1.show_role()