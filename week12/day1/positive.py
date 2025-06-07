"""Write a program that checks whether a number entered by the user is positive, negative, or zero."""
a=float(input("enter the number: "))
if (a>0):
    print(f"{a} is a positive number.")
elif(a==0):
    print(f"{a} is zero.")
else:
    print(f"{a} is negative number.")
