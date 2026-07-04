from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

c = CreditCard()
c.pay(100)
u = UPI()
u.pay(100)
        