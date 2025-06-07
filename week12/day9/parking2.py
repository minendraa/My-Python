import os
import datetime

class ParkingSystem:
    def __init__(self, log_file="parking.log", capacity=10):
        self.log_file = log_file
        self.capacity = capacity
        self.parked_vehicles = set()

        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as file:
                file.write("Parking log initialized\n")

    def get_parked_count(self):
        return len(self.parked_vehicles)

    def store_log(self, vehicle_number, owner, vtype, level="CHECK--IN--"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level}] Vehicle: {vehicle_number} | Owner: {owner} | Type: {vtype}\n"

        with open(self.log_file, 'a') as file:
            file.write(entry)

        print(f"Log recorded: {entry}", end='')

    def park_vehicle(self, vehicle_number, owner, vtype):
        if self.get_parked_count() >= self.capacity:
            print("Parking Full!")
            return

        if vehicle_number in self.parked_vehicles:
            print("Vehicle already parked.")
            return

        self.parked_vehicles.add(vehicle_number)
        self.store_log(vehicle_number, owner, vtype, "CHECK--IN--")

    def unpark_vehicle(self, vehicle_number):
        if vehicle_number not in self.parked_vehicles:
            print("Vehicle not found in parking.")
            return

        self.parked_vehicles.remove(vehicle_number)
        self.store_log(vehicle_number, "N/A", "N/A", "CHECK--OUT--")

    def view_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                data = file.readlines()

            if len(data) <= 1:
                print("No vehicles have been logged yet.")
            else:
                print("\n--- Parking Log Records ---")
                for line in data:
                    print(line, end='')
        else:
            print("Log file not found.")

    def filter_logs(self, keyword):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                lines = file.readlines()

            filtered = [line for line in lines if keyword.lower() in line.lower()]

            if filtered:
                print(f"\n--- Filtered Logs for '{keyword}' ---")
                for line in filtered:
                    print(line, end='')
            else:
                print(f"No matching records found for '{keyword}'.")
        else:
            print("Log file not found.")

if __name__ == "__main__":
    system = ParkingSystem(capacity=5)

    while True:
        print("\n--- Parking System Menu ---")
        print("1. Park Vehicle")
        print("2. Unpark Vehicle")
        print("3. View Logs")
        print("4. Filter Logs")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            vehicle = input("Enter vehicle number: ").strip().upper()
            owner = input("Enter owner name: ").strip().title()

            while True:
                print("Select vehicle type:")
                print("1. 2-wheeler")
                print("2. 4-wheeler")
                vtype_choice = input("Enter choice (1 or 2): ").strip()

                if vtype_choice == "1":
                    vtype = "2-wheeler"
                    break
                elif vtype_choice == "2":
                    vtype = "4-wheeler"
                    break
                else:
                    print("❌ Invalid choice. Please enter 1 or 2.")

            if vehicle and owner:
                system.park_vehicle(vehicle, owner, vtype)
            else:
                print("❗ Vehicle number and owner name cannot be empty.")


        elif choice == "2":
            vehicle = input("Enter vehicle number to unpark: ").strip().upper()
            if vehicle:
                system.unpark_vehicle(vehicle)
            else:
                print("Vehicle number cannot be empty.")

        elif choice == "3":
            system.view_logs()

        elif choice == "4":
            keyword = input("Enter keyword to filter (e.g., vehicle number, owner, type): ").strip()
            if keyword:
                system.filter_logs(keyword)
            else:
                print("Keyword cannot be empty.")

        elif choice == "5":
            print("Exiting Parking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
