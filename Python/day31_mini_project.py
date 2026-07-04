from abc import ABC, abstractmethod
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass
    def __init__(self,Food_name,Price,Preparing_Time):
        self.Food_name = Food_name
        self.Price = Price
        self.Preparing_Time = Preparing_Time
    def display_info(self):
        print(f"Food Name: {self.Food_name}")
        print(f"Price: {self.Price}")
        print(f"Preparing Time: {self.Preparing_Time}")
class Pizza(Food):
    def __init__(self, Food_name, Price, Preparing_Time):
        super().__init__(Food_name, Price, Preparing_Time)
    def prepare(self):
        pass
class Burger(Food):
    def __init__(self, Food_name, Price, Preparing_Time):
        super().__init__(Food_name, Price, Preparing_Time)
    def prepare(self):
        pass
class Biryani(Food):
    def __init__(self, Food_name, Price, Preparing_Time):
        super().__init__(Food_name, Price, Preparing_Time)
    def prepare(self):
        pass
items = [
    Pizza("Margherita", 8.99, "15 minutes"),
    Burger("Cheeseburger", 6.99, "10 minutes"),
    Biryani("Chicken Biryani", 9.99, "20 minutes")
]
for item in items:
    item.display_info()
    print()