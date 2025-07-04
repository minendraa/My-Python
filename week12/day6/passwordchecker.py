"""Simple Password Strength Checker
Concepts: Strings, Loops, Conditionals

Task:

Take a password input from the user.

Check for:

Minimum length (8)

Contains a number

Contains a symbol

Contains upper and lowercase letters

Return a strength level: Weak / Medium / Strong

what can be approach"""

def take_password():
    password=input("Enter the password: ")
    if len(password)>=8:
        return password
    else:
        print("The password must be equal or greater than 8 characters.")
        return take_password()

password=take_password()

def check(password):
    
    #global upper,lower,havenum,hasspecial
    
    upper = 0
    lower = 0
    havenum = 0
    hasspecial = 0

    for letter in password:
        if letter.isupper():
            upper = 1
        elif letter.islower():
            lower = 1
        elif letter.isdigit():
            havenum = 1
        elif not letter.isalnum():  
            hasspecial = 1

    if upper == 0:
        print("password should contain atleast 1 uppercase letter.")
        check(take_password())  
    elif lower == 0:
        print("password should contain atleast 1 lowercase letter.")
        check(take_password())
    elif havenum == 0:
        print("password should contain atleast 1 number.")
        check(take_password())
    elif hasspecial == 0:
        print("password should contain atleast 1 special character.")
        check(take_password())

    checkstrength(lower,upper,havenum,hasspecial) 

def entertwice(password):

    password2=input("Enter the password again: ")
    if password==password2:
        print(f"{password} has been set as your password.")
    else:
        print("Passwords does not match.. Please try again..")
        entertwice(password)


def checkstrength(lower,upper,havenum,hasspecial):

    if lower==1 and upper==1 and havenum==1 and hasspecial==1:
        print("Strong")
     
    elif lower==1 and upper==1 and havenum==1:
        print("Medium")
    elif lower==1 and upper==1:
        print("Weak")
    else:
        pass

    entertwice(password)

check(password)