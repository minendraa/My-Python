import random
secretnum=random.randint(1,20)
print("Welcome to the number game......")
usernum=int(input("enter your number: "))
attempt=1
while usernum!=secretnum:
    if(usernum>secretnum+5):
        print("too high")
    elif(usernum>secretnum):
        print("high")
    elif usernum<secretnum-5:
        print("too low")
    #elif usernum<secretnum:   
    else:
        print("low")
    usernum=int(input("enter your number: "))
    attempt+=1

if usernum==secretnum:
    print("You guessed it right")
print(f"You have attempted {attempt} times.")
#this is my game
