class Library:
    def __init__(self):
        self.books = {}     # key: bookno, value: dict with details + count
        self.borrowed = {}  # key: bookno, value: number of borrowed copies

    def add(self):
        try:
            nobooks = int(input("How many books do you want to add? "))
            for _ in range(nobooks):
                bookname = input("Enter the name of the book: ")
                bookno = int(input("Enter the book number: "))
                author = input(f"Enter the name of the author of '{bookname}': ")
                publication = input("Enter the publication name: ")
                copies = int(input("How many copies of this book? "))

                if bookno in self.books:
                    self.books[bookno]['count'] += copies
                    print(f"Added {copies} more copies of '{bookname}'. Total: {self.books[bookno]['count']}")
                else:
                    self.books[bookno] = {
                        "bookname": bookname,
                        "author": author,
                        "publication": publication,
                        "count": copies
                    }
                    print("Book added successfully!")
        except:
            print("Invalid input! Please try again.")

    def display(self):
        if not self.books:
            print("No books are currently available in the library.")
            return
        print("\nBooks available in the Library:")
        for i, (bookno, book) in enumerate(self.books.items(), start=1):
            print(f"\nBook {i}:")
            print(f"  Name: {book['bookname']}")
            print(f"  Book No: {bookno}")
            print(f"  Author: {book['author']}")
            print(f"  Publication: {book['publication']}")
            print(f"  Available Copies: {book['count']}")

    def borrow(self):
        if not self.books:
            print("No books are currently available in the library.")
            return
        try:
            bookno = int(input("Enter the book number you want to borrow: "))
            if bookno in self.books:
                available = self.books[bookno]['count']
                if available == 0:
                    print("All copies of this book are currently borrowed.")
                    return
                print(f"Available copies: {available}")
                copies = int(input("How many copies do you want to borrow? "))
                if copies <= available:
                    self.books[bookno]['count'] -= copies
                    self.borrowed[bookno] = self.borrowed.get(bookno, 0) + copies
                    print(f"Borrowed {copies} copy/copies of '{self.books[bookno]['bookname']}' successfully!")
                else:
                    print("Not enough copies available.")
            else:
                print("Book not found.")
        except:
            print("Please enter a valid number.")

    def returnborrowed(self):
        if not self.borrowed:
            print("No books have been borrowed.")
            return
        try:
            bookno = int(input("Enter the book number to return: "))
            if bookno in self.borrowed:
                print(f"Currently borrowed copies: {self.borrowed[bookno]}")
                copies = int(input("How many copies do you want to return? "))
                if copies <= self.borrowed[bookno]:
                    self.borrowed[bookno] -= copies
                    self.books[bookno]['count'] += copies
                    print(f"Returned {copies} copy/copies of '{self.books[bookno]['bookname']}' successfully.")
                    if self.borrowed[bookno] == 0:
                        del self.borrowed[bookno]
                else:
                    print("You're trying to return more than borrowed.")
            else:
                print("Book not found in borrowed list.")
        except:
            print("Please enter a valid number.")

    def delete(self):
        if not self.books:
            print("No books are currently available in the library.")
            return
        try:
            bookno = int(input("Enter the book number to delete: "))
            if bookno in self.borrowed:
                print(f"Book '{self.books[bookno]['bookname']}' is currently borrowed and cannot be deleted.")
                return
            if bookno in self.books:
                del self.books[bookno]
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        except:
            print("Please enter a valid book number.")

    def show_borrowed(self):
        if not self.borrowed:
            print("No books have been borrowed.")
            return
        print("\nBorrowed Books:")
        for bookno, count in self.borrowed.items():
            book = self.books[bookno]
            print(f"\nBook No: {bookno}")
            print(f"  Name: {book['bookname']}")
            print(f"  Borrowed Copies: {count}")

def operation():
    l1 = Library()

    while True:
        try:
            choice = int(input(
                "\nChoose an operation:\n"
                "1. Display available books\n"
                "2. Add books\n"
                "3. Borrow a book\n"
                "4. Return a book\n"
                "5. Delete a book\n"
                "6. Show borrowed books\n"
                "7. Quit\n"
                "Your choice: "
            ))

            if choice == 1:
                l1.display()
            elif choice == 2:
                l1.add()
            elif choice == 3:
                l1.borrow()
            elif choice == 4:
                l1.returnborrowed()
            elif choice == 5:
                l1.delete()
            elif choice == 6:
                l1.show_borrowed()
            elif choice == 7:
                print("Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 7.")
        except:
            print("Invalid input! Please enter a valid number.")

# Run the system
operation()
