import os
import datetime
class Attendance:
    def __init__(self,attendance_file="attendance.log"):
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

if __name__=="__main__":
    d1=Attendance()

d1.store_log("John Smith", level="CHECK--IN--")
d1.store_log("Emily Johnson", level="CHECK--IN--")
d1.store_log("John Smith", level="CHECK--OUT--")
d1.store_log("Emily Johnson", level="CHECK--OUT--")
d1.store_log("Michael Brown", level="CHECK--IN--")
d1.store_log("Olivia Davis", level="CHECK--IN--")
d1.store_log("Michael Brown", level="CHECK--OUT--")
d1.store_log("Olivia Davis", level="CHECK--OUT--")
d1.store_log("William Wilson", level="CHECK--IN--")
d1.store_log("William Wilson", level="CHECK--OUT--")


d1.view_logs()

d1.filter_data("CHECK--OUT--")

                