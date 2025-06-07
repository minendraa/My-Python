def take_studentinput():
    try: 
        name=input("Enter the student name: ")
        rollno=int(input("Enter the roll no of the student: "))
        phonenumber=input("Enter the phone number: ")
        address=input("Enter the address: ")
        print("Student info added..")

    except ValueError:
        print("Invalid input!!")
        return take_studentinput()
    
    print(f"Enter the marks of {name} according to the subjects: ")
    return name, rollno, phonenumber, address

