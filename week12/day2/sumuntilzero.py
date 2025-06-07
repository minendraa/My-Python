"""Sum Until Zero

Create a function that repeatedly asks the user for a number.
Keep a running total.

Stop when the user enters 0 and then return the sum."""

def sumofnumbers(numbers):
    print("The sum of all the numbers is: ",sum(numbers))   

def listing():
    numbers=[]
    i=int(input("Enter any number: "))
    while i!=0:
        numbers.append(i)
        i=int(input("Enter any number: "))
    if i==0:
        sumofnumbers(numbers)
listing()