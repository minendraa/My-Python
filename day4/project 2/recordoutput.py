import csv
def view():
    try:

        with open("studentrecords.csv", "r") as file:
            content = csv.reader(file)
            for row in content:
                print(row)
    
    except FileNotFoundError:
        print("The csv file is not created yet!!!")
    
        