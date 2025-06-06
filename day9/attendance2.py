import os
import datetime
class Attendance:
    def __init__(self,attendance_file="attendance2.log"):
        self.attendance_file=attendance_file
        if not os.path.exists(self.attendance_file):
            with open(self.attendance_file,'w')as file:
                file.write("Attendeance Record Initialized\n")
    
    def store_log(self,name,level="CHECK--IN--"):
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry=f"[{timestamp}] [{level}] {name.strip()}\n"

        with open(self.attendance_file,'a')as file:
            file.write(entry)

        print(f"Attendance recorded: {entry}",end='')

    def view_logs(self):
        if os.path.exists(self.attendance_file):
            with open(self.attendance_file,'r')as file:
                datas=file.read()

                print("\n Attendance Records Data")
                print(datas)

        else:
            print("Attendance does not exist..")
    
    def filter_data(self,keyword):
        if os.path.exists(self.attendance_file):
            with open(self.attendance_file,'r')as file:
                datas=file.readlines()

            filtered_data=[]

            for data in datas:
                if keyword in data:
                    filtered_data.append(data)

            print(f"Record containing '{keyword}'")
            for data in filtered_data:
                print(data,end='')

        else:
            print("This file does not exist")

if __name__ == "__main__":
    d1 = Attendance()

    while True:
        print("\n--- Attendance Menu ---")
        print("1. Record Attendance")
        print("2. View All Attendance Logs")
        print("3. Filter Attendance Records")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            name = input("Enter your name: ").strip()
            level_choice = input("Enter '1' for CHECK-IN or '2' for CHECK-OUT: ").strip()
            
            if level_choice == "1":
                level = "CHECK--IN--"
            elif level_choice == "2":
                level = "CHECK--OUT--"
            else:
                print("Invalid level choice. Please try again.")
                continue

            d1.store_log(name, level)

        elif choice == "2":
            d1.view_logs()

        elif choice == "3":
            keyword = input("Enter keyword to filter (e.g., name or CHECK--IN--): ").strip()
            d1.filter_data(keyword)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
