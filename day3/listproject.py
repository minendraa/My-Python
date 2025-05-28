def takemarks():
    marks=[]
    for i in range(10):
        m=float(input("enter the marks of student: "))
        if m>0 and m<=100:
            marks.append(m)
        else:
            print("Please enter marks above 0 and below 100") 
    return marks

marks=takemarks()

def check(marks):
    print("All marks: ")
    print(marks)
    highestmarks=max(marks)
    print("Highest mark= ",highestmarks)
    lowestmarks=min(marks)
    print("Lowest marks = ",lowestmarks)
    averagemarks=sum(marks)/len(marks)
    print("average marks of all: ",averagemarks)

    print("List of top 3 marks: ")
    markss=sorted(marks,reverse=True)
    marksss=markss[:3]
    print(marksss)
    passed=[]
    for k in markss:
        if k>40:
            passed.append(k)
        else:
            pass
    print("Number of passed students in the class.")
    print(len(passed))

check(marks)