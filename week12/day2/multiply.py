"""Multiplication Quiz
Write a function quiz() that randomly generates multiplication problems.

Ask the user 5 questions using a while loop.

Track and print the number of correct answers at the end."""

import random
def quiz():
    i=1
    correctans=0
    incorrect=0
    while i<=5:
        num1=random.randint(1,10)
        num2=random.randint(1,10)

        ans=int(input(f"{num1} x {num2} = "))
        if ans==num1*num2:
            print("Correct answer")
            i+=1
            correctans+=1
        else:
            print("Incorrect answer")
            i+=1
            incorrect+=1
    print(f"You answered {correctans} correctly and {incorrect} incorrectly.")
    print("--------End of the Quiz--------")
quiz()