from datetime import datetime 
bookname=[]
date=[]
author=[]
readstatus=[]
def take_input():
        nameofbook=input(f"Enter the name of the book {len(bookname)+1}: ")
        nameofauthor=input("Enter the name of the author: ")
        status=int(input("Enter '1' if read or Enter '2' if left to read: "))
        if status==1:
            readstatus.append("Read")
        elif status==2:
            readstatus.append("Not read Yet...")
        else: 
            print("Invalid input!! Please enter '1' if read or Enter '2' if left to read.\n")
            return            
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bookname.append(nameofbook.capitalize())
        author.append(nameofauthor.capitalize())
        date.append(today)
        print("------Listed in the Library System------\n")

def check():
    print("-----Welcome to your Personal Book Library Manager-----")
    while True:
        choice=int(input("Enter 1 to view your reading history, Enter 2 to add new readings, Enter 3 to delete a listing, enter 4 to quit.. \n"))
        if choice==1:
            if len(bookname)>0:
                    for a in range(len(bookname)):
                        print(f"Details of book no.{a+1}: ")
                        print(f"Book Title: {bookname[a]}")
                        print(f"Author: {author[a]}")
                        print(f"Status: {readstatus[a]}")
                        print(f"Date: {date[a]}\n")
            else:
                print("The list is empty!!!")    

        elif choice==2:
            take_input()

        elif choice==3:
            removebook=input("Enter the name of the book you would like to remove: ")
            removeebook=removebook.capitalize()
            try:
                if removeebook in bookname:
                    l=bookname.index(removeebook)
                    bookname.pop(l)
                    author.pop(l)
                    date.pop(l)
                    readstatus.pop(l)
                    print(f"{removeebook} has been removed from the list.. ")
            except:
                print(f"Error! did not find any book with the name {removeebook} in your library.")
                return
            
        elif choice==4:
            return

        else: 
            print("Enter number between 1 to 3 to run any operations!!!")

check()