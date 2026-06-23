class Phone:
    def __init__(self,Brand,Model,Price):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price
class Phone2:
    def __init__(self):
        self.phone = []

    def add_phone(self,phone):
        self.phone.append(phone)

    def wanted(self):
        for phone in self.phone:

            print("Brand :" ,phone.Brand)
            print("Model :",phone.Model)
            print("Price :",phone.Price)
            print("_"*30)

p1 = Phone("Samsung","S24",75000)
p2 = Phone("Apple","iphone 16",90000)
p3 = Phone("OnePlus","13",65000)

manager = Phone2()

manager.add_phone(p1)
manager.add_phone(p2)
manager.add_phone(p3)

manager.wanted()