import csv
def view():
    with open("studentrecords.csv", "r") as file:
        content = csv.reader(file)
        for row in content:
            print(row)