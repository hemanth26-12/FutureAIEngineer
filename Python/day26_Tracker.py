class InternTracker:
    def __init__(self,Company,Role,Stipend,Status):
        self.Company = Company
        self.Role= Role
        self._Stipend = Stipend
        self.Status = Status

class InternshipTracker: 
   def __init__(self):
      self.internship = []
   def add_internship(self,internship):
      self.internship.append(internship)
   def show(self):
      for internship in self.internship:
         
        print("Company :",internship.Company)
        print("Role :",internship.Role)
        print("Stipend :",internship._Stipend)
        print("Status :", internship.Status)
        print("-"*30)

e1 = InternTracker("Google","Python Intern",10000,"Applied")
e2 = InternTracker("Amazon","Developer",15000,"Applied")
tracker = InternshipTracker()

tracker.add_internship(e1)
tracker.add_internship(e2)
tracker.show()


