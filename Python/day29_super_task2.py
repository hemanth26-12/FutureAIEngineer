class Employee:
    def __init__(self,Name):
        self.Name = Name


class AIEngineer(Employee):
    def __init__(self, Name,Skill):
        super().__init__(Name)
        self.Skill = Skill

        print('Name :',self.Name)
        print('Skill', Skill)

a1 = AIEngineer("Hemanth","Machine Learning")
