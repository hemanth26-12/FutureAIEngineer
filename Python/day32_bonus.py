class FuelLowError(Exception):
    pass
class intern:
    def __init__(self, Rocket_Name, Fuel, Destination):
        self.Rocket = Rocket_Name
        self.Fuel = Fuel
        self.Destination = Destination

        if self.Fuel < 20:
            raise FuelLowError("Fuel is low needed to fill it.")
        else:
            print("Launch Ready")

    def display(self):
        print(f"Rocket Name : {self.Rocket}")
        print(f"Fuel : {self.Fuel}%")
        print(f"Destination : {self.Destination}")


rockets = [
    ("Chandrayan", 50, "Moon"),
    ("Chandrayan2", 30, "Mars"),
    ("Chandrayan3", 80, "Mars"),
    ("Chandrayan", 20, "Mercury"),
    ("Chandrayan2", 10, "Jupiter")
]

for name, fuel, destination in rockets:
    try:
        rocket = intern(name, fuel, destination)
        rocket.display()
    except FuelLowError as e:
        print(e)
    print()

    

