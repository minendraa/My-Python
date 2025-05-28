def inputt():
    sentence=input("enter the text: ")
    return sentence
    
def check(sentence):
    uppercase=sentence.upper()
    firstlettercapital=sentence.capitalize()
    l=input("enter the letter you would liken to count")
    counting=sentence.count(l)
    return uppercase, firstlettercapital, counting,l
    
sentence=inputt()
uppercase, firstlettercapital, counting,l = check(sentence)
print(f"{uppercase}")
print(f"{firstlettercapital}")
print(f"You have {counting} '{l}'s.")