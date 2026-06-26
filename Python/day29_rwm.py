class Employee:
    def __init__(self,name):
        self.name = name

class SecurityOfficer(Employee):
    def __init__(self, name,shift):
        super().__init__(name)
        self.shift = shift

class AISecurityOfficer(SecurityOfficer):
    def __init__(self, name, shift,AI_Tool):
        super().__init__(name, shift)
        self.AI_Tool = AI_Tool

        print("Name :",self.name)
        print("Shift :",self.shift)
        print("AI Tool :",AI_Tool)


a1 = AISecurityOfficer("Hemanth","Night","ChatGPT")
a2 = AISecurityOfficer("Ravi","Morning","Gemini")
        