"""Activities:
Part 1: Base Class – Vehicle
Attributes: brand, year
Method:
info() → prints: "This is a <brand> made in <year>."
Part 2: Derived Class – Car(Vehicle)
Extra attributes: model, seats
Use super().__init__(brand, year)
Method:
drive() → prints: "Driving a <brand> <model> with <seats> seats."
Part 3: Derived Class – Truck(Vehicle)
Extra attributes: capacity_tons, wheels
Use super().__init__(brand, year)
Method:
haul() → prints: "The <brand> truck is hauling <capacity_tons> tons with <wheels> wheels."""

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"This is a {self.brand} made in {self.year}.")

class Car(Vehicle):
    def __init__(self, brand, year, model, seats):
        super().__init__(brand, year)
        self.model = model
        self.seats = seats

    def drive(self):
        print(f"Driving a {self.brand} {self.model} with {self.seats} seats.")

class Truck(Vehicle):
    def __init__(self, brand, year, capacity_tons, wheels):
        super().__init__(brand, year)
        self.capacity_tons = capacity_tons
        self.wheels = wheels

    def haul(self):
        print(f"The {self.brand} truck is hauling {self.capacity_tons} tons with {self.wheels} wheels.")

c1 = Car("Chevrolet", 2012, "Optra LT", 5)
c1.info()
c1.drive()
print(id(c1.brand))
# c2 = Car("Hyundai", 2025, "Verna", 5)
# c2.info()
# c2.drive()

# t1 = Truck("Tata", 2020, 5, 6)
# t1.info()
# t1.haul()

c1.seats=4
c1.info()
c1.drive()

print(id(c1.brand))