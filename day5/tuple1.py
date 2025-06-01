print("Welcome to the tuple system")

tuple1=()

def indexing(tuple1:tuple):
    try:
        i = input("Enter the element to find the index of the first occurrence: ")
        print(f"Index of '{i}' is: ")
        a=(tuple1.index(i))
        print(a+1)
    except:
        print("Element not in tuple")

def counting(tuple1:tuple):
    a = input("Enter the element you want to check the count of the occurrences: ")
    print(f"Count of '{a}':", tuple1.count(a))

def check():
    while True:
        print("Enter \n1 to input the elements in the tuple \n2 to find the occurrence \n3 to check the count of the given element \n4 to quit")
        choice = int(input("= "))
        if choice in range(1, 5):
            if choice == 1:
                global lists
                lists = []
                i = 1
                num = int(input("Enter the number of elements you want to keep: "))
                for _ in range(num):
                    a = input(f"Enter element {i}: ")
                    lists.append(a)
                    i += 1
                global tuple1
                tuple1 = tuple(lists)
                print(tuple1)

            elif choice == 2:
                indexing(tuple1)
                
            elif choice == 3:
                counting(tuple1)
                
            else:
                return
        else:
            print("Enter a valid number....")

check()