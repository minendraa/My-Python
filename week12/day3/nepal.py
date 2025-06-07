sentence="aaaabcd"
s=sentence.replace("a","c")
count=0
for x in s:
    if x=="c":
        count+=1
    else:
        pass
print(count)