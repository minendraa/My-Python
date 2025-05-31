import csv

# Function to initialize the CSV file
def initialize_csv(file_name):
    with open(file_name, mode='a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Description", "Amount"])

# Function to add an expense
def add_expense(file_name, category, description, amount):

    with open(file_name, mode='a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([category, description, amount])
        
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses(file_name):
    try:
        with open(file_name, mode='r') as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
        print("No expenses recorded yet!")

# Function to calculate total expenses
def calculate_total(file_name):
    total = 0.0
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                total = total + float(row[2])  # Amount is in the 3rd column

    except:
        print("No expenses recorded yet!")
        return

    print(f"Total Expenses: {total}")