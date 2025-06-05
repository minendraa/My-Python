class Library:
    def __init__(self,bookname,bookno,author,publication):
        self.bookname=bookname
        self.book_no=bookno
        self.author=author
        self.publication=publication
    
    def add(self):
        nobooks=int(input("How many books do you want to add? "))
        for a in range(nobooks):
            print(f"Adding the book no {a+1}: ")
            try: 
                bookname=input("Enter the name of the book: ")
                bookno=int(input("Enter the bookno: "))
                author=input(f"Enter the name of the author of the book {bookname}: ")
                publication=input("Enter the publication name: ")
            except:
                print("Invalid input!! Please try again.")
                return
    
    def display(self):
        print("The books available in the Library are as follows: ")
        print

    def borrow(self):
        


def operation():
    choice=int(input("Enter \n1 for displaying the items \n2 for adding a book \n3 for borrowing book"))
    if x in range(choice):
        if x==1:
            Library.display()

        elif x==2:
            Library.add()

        elif x==3:
            Library.borrow()

