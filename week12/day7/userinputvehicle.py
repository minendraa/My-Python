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
        print(f"Driving a {self.brand} {self.model} with {self.seats} seats.\n")

class Truck(Vehicle):
    def __init__(self, brand, year, capacity_tons, wheels):
        super().__init__(brand, year)
        self.capacity_tons = capacity_tons
        self.wheels = wheels

    def haul(self):
        print(f"The {self.brand} truck is hauling {self.capacity_tons} tons with {self.wheels} wheels.\n")


num_cars = int(input("Enter number of cars: "))
cars = []

for i in range(num_cars):
    print(f"\nEnter details for Car {i+1}:")
    brand = input("Brand: ")
    year = int(input("Year: "))
    model = input("Model: ")
    seats = int(input("Seats: "))
    car = Car(brand, year, model, seats)
    cars.append(car)

num_trucks = int(input("\nEnter number of trucks: "))
trucks = []

for i in range(num_trucks):
    print(f"\nEnter details for Truck {i+1}:")
    brand = input("Brand: ")
    year = int(input("Year: "))
    capacity = float(input("Capacity in tons: "))
    wheels = int(input("Number of wheels: "))
    truck = Truck(brand, year, capacity, wheels)
    trucks.append(truck)


print("\n--- Car Details ---")
for car in cars:
    car.info()
    car.drive()

print("\n--- Truck Details ---")
for truck in trucks:
    truck.info()
    truck.haul()