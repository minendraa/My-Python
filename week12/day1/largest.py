"""Write a Python program to find the largest of three numbers entered by the user."""
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=float(input("Enter the third number: "))

if(a>b and a>c):
    print(f"{a} is the largest number.")
elif (b>c and b>a):
    print(f"{b} is the largest number. ")
else:
    print(f"{c} is the largest number.")
    