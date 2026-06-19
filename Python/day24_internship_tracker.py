class InternTracker:
    def intern_ships(self,Company,Role,Stipend,Status):
        self.Company = Company
        print("Company :",self.Company)
        self.Role= Role
        print("Role :",self.Role)
        self._Stipend = Stipend
        print("Stipend :",self._Stipend)
        self.Status = Status
        print("Status :", self.Status)
e1 = InternTracker()
e2 = InternTracker()


e1.intern_ships("Google","Python Intern",10000,"Applied")
e2.intern_ships("Amazon","Developer",15000,"Applied")
e2.intern_ships("FilpKart","Developer",11000,"Progressing")
e2.intern_ships("Amazon","Developer",15000,"Not Applied Yet")

