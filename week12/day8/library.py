class Library:
    def __init__(self):
        self.books = []
        self.borrowed=[]

    def add(self):
        try:
            nobooks = int(input("How many books do you want to add? "))
            for a in range(nobooks):
                print(f"\nAdding book no {a+1}: ")
                bookname = input("Enter the name of the book: ")
                bookno = int(input("Enter the book number: "))
                author = input(f"Enter the name of the author of '{bookname}': ")
                publication = input("Enter the publication name: ")
                book = {
                    "bookname": bookname,
                    "bookno": bookno,
                    "author": author,
                    "publication": publication
                }
                self.books.append(book)
                print("Book added successfully!")
        except:
            print("Invalid input! Please try again.")

    def display(self):
        if not self.books:
            print("No books are currently available in the library.")
            return
        print("\nThe books available in the Library are as follows:")
        for i, book in enumerate(self.books, start=1):
            print(f"\nBook {i}:")
            print(f"  Name: {book['bookname']}")
            print(f"  Book No: {book['bookno']}")
            print(f"  Author: {book['author']}")
            print(f"  Publication: {book['publication']}")

    def borrow(self):
        if not self.books:
            print("No books are currently available in the library.")
            return
        try:
            bookno = int(input("Enter the book number of the book you want to borrow: "))
            for book in self.books:
                if book["bookno"] == bookno:
                    self.books.remove(book)
                    self.borrowed.append(book)
                    print(f"Borrowed '{book['bookname']}' successfully!")
                    return
            print("Book not found.")
        except:
            print("Please enter a valid book number.")
    
    def returnborrowed(self):
        if not self.borrowed:
            print("No books have been borrowed. ")
            return
        try:
            bookno=int(input("Enter the book no you want to return: "))
            for book in self.borrowed:
                if book["bookno"] == bookno:
                    self.borrowed.remove(book)
                    self.books.append(book)
                    print(f"Returned '{book['bookname']}' successfully")
                    return
                
                print("Book not found in the borrowed list.")
        except:
            print("Please enter a vlid book number. ")

    def delete(self):
        if not self.books:
            print("No books are currently available in the library.")
            return
        try:
            bookno=int(input("Enter the book no you want to delete: "))
            for book in self.borrowed:
                if book["bookno"] == bookno:
                    print(f"Book '{book['bookname']}' is borrowed cannot delete. ")
                    return
                
            for book in self.books:
                if book["bookno"] == bookno:
                    self.books.remove(book)
                    print(f"Deleted '{book['bookname']}' successfully!")
                    return
                
            print("Book not found.")

        except:
            print("Please enter a valid book number.")

def operation():
    l1 = Library()

    while True:
        try:
            choice = int(input("Enter:\n1 for displaying the books\n2 for adding a book\n3 for borrowing a book\n4 to return the borrowed book \n5 to delete \n 6 to quit \nYour choice: "))
            if choice == 1:
                l1.display()
            elif choice == 2:
                l1.add()
            elif choice == 3:
                l1.borrow()
            elif choice == 4:
                l1.returnborrowed()
            elif choice==5:
                l1.delete()
            elif choice==6:
                print("Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 4.")
        except:
            print("Invalid input! Please enter a valid number.")

operation()
