import csv

expenses=[]

def dataoutput():
    with open("dataa.csv", "r") as file:
      
        reader = csv.reader(file)
        next(reader)

        expenditure1=0

        for row in reader:
            expenditure1=(float(row[1]))
            expenses.append(expenditure1)
        
    print(f"The sum of all the expenses is: {sum(expenses)}")
