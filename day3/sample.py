#inventory management system 
"""add remove specific item to inventory, check if inventory is empty or not if not empty list total number of items"""
print("Welcome to the Simple Inventory system")
def take_input():
    global n
    n=int(input("Enter how many items you would like to store: "))
    items_name=[]
    for i in range(n):
        item=input("Enter item name: ")
        items_name.append(item)
    print("All the items are: ")
    print(items_name)
    return items_name

items_name=take_input()

def check(items_name):
    while True:
        p=int(input("enter 1 for adding items, 2 for removing items and 3 for checking if the inventory is empty or not and 4 to exit: "))
        if p==1:
            newitem=input("Enter the name of the item: ")
            items_name.append(newitem)
            print(items_name)
        elif p==2:
            removeitem=input("Enter the name of the item you would like to remove: ")
            items_name.remove(removeitem)
            print(items_name)
        elif p==4:
            print("Thanks for using!!!")
            break
        elif p==3:
            count=len(items_name)
            for x in range(n):
                if x>0:
                    print(f"The inventory is not empty there are {count} number of items.")
                    print(items_name)

                else:
                    print("there are no items left in the inventory. ")
        
        else:
            print("Invalid input!! Please enter the value between 1 to 4. ")
            break
        
check(items_name)

