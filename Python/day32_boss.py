class InvalidAmountError(Exception):
    pass
class InsufficientBalanceError(Exception):
    pass
class Account:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.errors = []
    def deposit(self, amount):
        if amount <= 0:
            self.errors.append(InvalidAmountError("Deposit amount must be greater than zero."))
            return
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            self.errors.append(InvalidAmountError("Withdrawal amount must be greater than zero."))
            return
        if amount > self.balance:
            self.errors.append(InsufficientBalanceError("Insufficient balance for the withdrawal."))
            return
        self.balance -= amount
    def display(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        if self.errors:
            print("Errors:")
            for e in self.errors:
                print(" -", e)
        print()
def main():
    a = Account("Hemanth", 2000, 113457648)
    b = Account("Ravi", 15000, 423637892)
    c = Account("Ramesh", 25000, 765342689)
    d = Account("Shiva", 500, 987654321)
    e = Account("Anita", 1200, 192837465)
    a.deposit(2500)
    a.withdraw(10000)   
    b.deposit(2500)
    b.withdraw(3000)
    c.deposit(2500)
    c.withdraw(5000)
    d.withdraw(-100)    
    e.deposit(0)        
    accounts = [a, b, c, d, e]
    for i, acc in enumerate(accounts, start=1):
        print(f"Account {i} details:")
        acc.display()
if __name__ == '__main__':
    main()


