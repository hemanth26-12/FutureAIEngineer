class Expense:
    def __init__(self, Details):
        self.Details = Details

    def details(self):
        print("Food :", self.Details["Food"])
        print("Travel :", self.Details["Travel"])
        print("Internet :", self.Details["Internet"])
        print("--" * 30)

expenses = [
    Expense({
        "Food": 500,
        "Travel": 300,
        "Internet": 700
    }),
    Expense({
        "Food": 400,
        "Travel": 200,
        "Internet": 600
    }),
    Expense({
        "Food": 450,
        "Travel": 250,
        "Internet": 650
    })
]

for expense in expenses:
    total = expense.Details["Food"] + expense.Details["Travel"] + expense.Details["Internet"]
    print("Total :", total)
    expense.details()

    






        
        