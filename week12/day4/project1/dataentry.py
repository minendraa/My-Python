from datetime import datetime
import csv

write_header=False

def Take_income_and_expenses(filename):    
    global write_header
    
    try:
        Category = input("Enter category: ")
        expenditure = float(input("Enter your expense: "))
        description = input("Enter the description for your expense: ")
    except ValueError:
        print("Invalid input! Please enter correct data types.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        if write_header==True:
            with open(filename, mode='a', newline='') as csvfile:
                writer = csv.writer(csvfile)                
                writer.writerow([Category, expenditure, description, date])
        elif write_header==False:
            with open(filename, mode='w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Category', 'expenditure', 'Description', 'Date'])
                writer.writerow([Category, expenditure, description, date])
                write_header = True
        else:
                return
    except FileNotFoundError:
          
        print(f"Data saved to {filename}\n")

