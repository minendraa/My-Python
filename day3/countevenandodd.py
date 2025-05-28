def takeinput():
    numbers=[]
    for i in range(10):
        num=int(input("enter the numbers: "))
        numbers.append(num)
    return numbers

numbers=takeinput()

def check(numbers):
    even=0
    odd=0
    for n in numbers:
        if n%2==0:
            even+=1
        else:
            odd+=1
    print(f"{even} are even and {odd} are odd.")

check(numbers)
    