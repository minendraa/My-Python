from datetime import datetime
expense=[]
price=[]
date=[]

def take_expense():
    expenseeinput=input(f"Enter the expense cause {len(expense)+1}: ")
    expenseinput=expenseeinput.capitalize()
    expense.append(expenseinput)
    return expense
   
def take_price():
    priceinput=float(input("Enter the price of this expense: "))
    price.append(priceinput)
    return price

def dateofexpense():
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date.append(today)
    return date

def check():
    print("-----Welcome to Daily expense Tracker-----")
    expense=take_expense()
    price=take_price()
    date=dateofexpense()
    while True:
        print("Enter 1 for Viewing your expenses, 2 for adding expenses, 3 for deleting expenses and 4 to quit")
        i=int(input("= "))
        if i==1:
            print("Your All expenses is: ")
            for i in range(len(expense)):
                print(f"Expense {i+1}: {expense[i]}")
                print(f"Price: {price[i]}")
                print(f"Date: {date[i]}\n")

        elif i==2:
            print("Add Expense: ")
            take_expense()
            take_price()
            dateofexpense()

        elif i==3:
            print("What expense would you like to remove: ")
            itemname=input("= ")
            itemsname=itemname.capitalize()
            positioning=expense.index(itemsname)
            expense.pop(positioning)
            price.pop(positioning)
            date.pop(positioning)
            print(f"'{itemsname}' has been removed.")

        elif i==4:
            print("Thanks for using our program....!!!!")
            break

check()