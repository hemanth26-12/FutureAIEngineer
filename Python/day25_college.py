class College:
    def __init__(self,Details):
        self.Details = Details

    def details(self):
        print("Name :",self.Details["Name"])
        print("Roll :",self.Details["Roll"])
        print("Marks :",self.Details["Marks"])
        print("--"*30)

students = [
    College({
        "Name": "Hemanth",
        "Roll": 420,
        "Marks": 99
    }),
    College({
        "Name": "rahul",
        "Roll": 421,
        "Marks": 90
    }),
    College({
        "Name": "daru",
        "Roll": 42,
        "Marks": 90
    })
]

for student1 in students:
    student1.details()






        
        