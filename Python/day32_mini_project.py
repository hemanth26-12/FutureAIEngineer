class InvaildStatusError(Exception):
    pass
class JobApplication:
    def __init__(self, Company, Role, Status):
        if Status not in ["Applied", "Interview", "Selected", "Rejected"]:
            raise InvaildStatusError("the status were not able to tracking")
        self.Company = Company
        self.Role = Role
        self.Status = Status
    def display(self):
        print(f"Company :{self.Company}")
        print(f"Role :{self.Role}")
        print(f"Status :{self.Status}")
a = [
    JobApplication("Amazon","HR","Applied"),
    JobApplication("Flipkart","Manager","Interview"),
    JobApplication("FIFO","Tester","Selected"),
    JobApplication("Wipro","HR","Rejected"),
    JobApplication("Infosys","HR","Selected")
]
for i in a:
    i.display()
    print()
      