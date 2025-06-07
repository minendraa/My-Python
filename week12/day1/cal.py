"""Create a simple calculator using if-else that performs addition, subtraction, multiplication, or division based on the user's choice."""
print("Simple calculator")
loops = 1
a=int(input("Enter \n 1 for addition \n 2 for substraction \n 3 for multiplication \n 4 for division \n 5 for exit = "))
def getinput():
    num1=float(input("enter first number: "))
    num2=float(input("enter second number: "))
    return num1,num2

while loops==1:
  
    if (a==1):
        num1,num2=getinput()
        print(f"The sum of {num1} and {num2} is {num1+num2}")
    elif (a==2):
        num1,num2=getinput()
        print(f"The difference of {num1} and {num2} is {num2-num1}")
    elif (a==3):
        num1,num2=getinput()
        print(f"The product of {num1} and {num2} is {num2*num1}")
    elif (a==4):
        num1,num2=getinput()
        print(f"The division of {num1} and {num2} is {num1/num2}")
    elif (a==5):
        continue
    else:
        print("invalid input!! please enter number between 1 to 5") 
        break