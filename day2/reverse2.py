def takeinput():
    i=int(input("Enter the number: "))
    return i
def reversee(i):
    a=str(i)
    m=[]
    for n in a:
        m.append(n)
        m.reverse()
    z=""
    for j in m:
        u=str(j)
        z+=u

    print(z)

i=takeinput()
reversee(i)
