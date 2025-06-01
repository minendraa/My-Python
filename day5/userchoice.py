"""Create a dictionary.
Add, update, or delete a key-value pair.
Access elements by key.
Iterate over keys and values."""


def create_dict():
    global bike
    bike={
        "make":"YAMAHA",
        "year":2025,
        "displacement":"1000cc",
        "color":"Yamaha Blue",
        "chasis no":"1234CN"
    }

create_dict()

def addvalues():
    inputkey=input("Enter the key: ")
    inputvalue=input("Enter the value: ")
    bike[inputkey]=inputvalue
    print(f"Successfully added {inputkey}")

    
def update():
    inputkey=input("Enter the key: ")
    inputvalue=input("Enter the value: ")
    bike.update({inputkey:inputvalue})
    print(f"Successfully updated {inputkey}")

def delete():
    inputkey=input("Enter the key you want to delete: ")
    bike.pop(inputkey)
    print(f"Successfully deleted {inputkey}")


def accesselement():
    inputkey=input("Enter the key you want to check: ")
    print(bike.get(inputkey))
    

def printwhole():
    print(bike.items())
def printkeys():
    print(bike.keys())


def check():
    print("Enter \n1 to print the dictionary  \n2 to add item \n3 to update the value for the given key \n4 to delete the item \n5 to access the given element \n6 to quit")
    choose=int(input("= "))

    if choose in range(1,7):  
            if choose==1:
                printwhole()
            elif choose==2:
                printkeys()
                addvalues()
            elif choose==3:
                printkeys()
                update()
            elif choose==4:
                printkeys()
                delete()
            elif choose==5:
                printkeys()
                accesselement() 
    else:
        print("Invalid input please try again")
        return check()
     
check()