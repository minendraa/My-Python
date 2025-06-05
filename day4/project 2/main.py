""""Student Gradebook Management System"
Build a Python program that allows teachers to manage student records, including adding student details, recording grades, calculating averages, and 
generating report cards. 
The system should use file I/O to store data, modular design for different components (e.g., student, grades, reports), and exception handling for 
invalid inputs or missing files."""

import csv,os
from Studentdetails import take_studentinput
from calculations import Calculations
from recordoutput import view

filename="studentrecords.csv"

def check(filename):
    i=int(input("Enter the number of students in Class: ")) 
    a=1
   
    for x in range(i):
        print(f"Enter the student details here for Student {a}: ")
        a+=1
        if (os.path.exists(filename))==False:
            name,rollno,phonenumber,address=take_studentinput()
            subject1,subject2,subject3,subject4,average_marks_obtained,Grade=Calculations()
            with open(filename,mode='w',newline='')as file:
                writer=csv.writer(file)
                writer.writerow(["Roll Number, Name, Phonenumber, Address, Marks in C, Marks in C++, Marks in java, Marks in python, Average Marks Obtained, Grade"])
                writer.writerow([rollno,name,phonenumber,address,subject1,subject2,subject3,subject4,average_marks_obtained,Grade])
                (os.path.exists(filename))==True
                
        else:
            name,rollno,phonenumber,address=take_studentinput()
            subject1,subject2,subject3,subject4,average_marks_obtained,Grade=Calculations()
            with open(filename,mode='a',newline='')as file:
                writer=csv.writer(file)
                #writer.writerow(["Roll Number, Name, Phonenumber, Address, Marks in C, Marks in C++, Marks in java, Marks in python, Average Marks Obtained, Grade"])
                writer.writerow([rollno,name,phonenumber,address,subject1,subject2,subject3,subject4,average_marks_obtained,Grade])

def choice():
    print("-----Welcome to the Students Record book-----")
    print("Enter\n 1 to input the student details\n 2 to view the records\n 3 to quit ")
    choose=int(input("Enter the number: "))
    if choose in range(1,4):
        if choose==1:
            check(filename)
            return choice()
        elif choose==2:
            view()
            return choice()
        else: 
            print("Thanks for using our system.")
    else:
        print("Invalid input please try again.")
        return choice()

choice()