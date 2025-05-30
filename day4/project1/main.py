import csv
from dataentry import Take_income_and_expenses
from dataoutput import dataoutput


filename = 'dataa.csv'

def check():
    while True:
        print("Enter what would you like to perform.")
        print("Enter \n1 to add the data \n2 to retrive data \n3 to exit")
        choice=int(input("= "))
        if choice==1:
            Take_income_and_expenses(filename)
        elif choice==2:
            dataoutput()
        elif choice==3:
            break
        else:
            print("Enter a valid number!!!")
            return
        
check()