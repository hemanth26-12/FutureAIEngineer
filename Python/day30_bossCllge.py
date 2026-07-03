class person:
    def __init__(self,name):
        self.name = name      
class Doctor:
    def __init__(self,Department):
        self.Department = Department      
    def diagnose(self):
        print("Diagnosing...")
class Researcher:
    def __init__(self,research_area):
        self.research_area = research_area      
    def research(self):
        print("Researching...")
class AISpecialist(Doctor,Researcher):
    def __init__(self,name,Department,research_area):
        person.__init__(self,name)
        Doctor.__init__(self,Department)
        Researcher.__init__(self,research_area)
    def show_details(self):
        print("Name :",self.name)
        print("Department :",self.Department)
        print("Research Area :",self.research_area)
        self.diagnose()
        self.research()
c1 = AISpecialist(name="Hemanth",Department="Cardiology",
                  research_area="AI in Healthcare")
c1.show_details()