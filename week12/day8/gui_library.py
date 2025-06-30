import streamlit as st

def init_library():
    if 'books' not in st.session_state:
        st.session_state.books = {}     # bookno -> dict with details + count
    if 'borrowed' not in st.session_state:
        st.session_state.borrowed = {}  # bookno -> borrowed count

def add_book():
    st.subheader("Add Books")
    with st.form("add_form"):
        nobooks = st.number_input("How many books do you want to add?", min_value=1, step=1)
        submitted = st.form_submit_button("Add Books")
        if submitted:
            for _ in range(nobooks):
                st.info(f"Enter details for book {_+1}")
                bookname = st.text_input("Enter book name", key=f"add_bookname_{_}")
                bookno = st.number_input("Enter book number", min_value=1, step=1, key=f"add_bookno_{_}")
                author = st.text_input("Enter author name", key=f"add_author_{_}")
                publication = st.text_input("Enter publication", key=f"add_publication_{_}")
                copies = st.number_input("Number of copies", min_value=1, step=1, key=f"add_copies_{_}")
                
                # Add to library
                if bookno in st.session_state.books:
                    st.session_state.books[bookno]['count'] += copies
                    st.success(f"Added {copies} more copies of '{bookname}'. Total copies: {st.session_state.books[bookno]['count']}")
                else:
                    st.session_state.books[bookno] = {
                        "bookname": bookname,
                        "author": author,
                        "publication": publication,
                        "count": copies
                    }
                    st.success(f"Book '{bookname}' added successfully!")

def display_books():
    st.subheader("Available Books")
    if not st.session_state.books:
        st.info("No books are currently available in the library.")
        return
    for bookno, book in st.session_state.books.items():
        st.markdown(f"**Book No:** {bookno}")
        st.markdown(f" - Name: {book['bookname']}")
        st.markdown(f" - Author: {book['author']}")
        st.markdown(f" - Publication: {book['publication']}")
        st.markdown(f" - Available Copies: {book['count']}")
        st.markdown("---")

def borrow_book():
    st.subheader("Borrow Book")
    if not st.session_state.books:
        st.info("No books available to borrow.")
        return
    bookno = st.number_input("Enter the book number you want to borrow", min_value=1, step=1)
    if bookno not in st.session_state.books:
        st.warning("Book not found.")
        return
    available = st.session_state.books[bookno]['count']
    st.write(f"Available copies: {available}")
    if available == 0:
        st.warning("All copies of this book are currently borrowed.")
        return
    copies = st.number_input("How many copies do you want to borrow?", min_value=1, max_value=available, step=1)
    if st.button("Borrow"):
        st.session_state.books[bookno]['count'] -= copies
        st.session_state.borrowed[bookno] = st.session_state.borrowed.get(bookno, 0) + copies
        st.success(f"Borrowed {copies} copy/copies of '{st.session_state.books[bookno]['bookname']}' successfully!")

def return_book():
    st.subheader("Return Book")
    if not st.session_state.borrowed:
        st.info("No books have been borrowed.")
        return
    bookno = st.number_input("Enter the book number to return", min_value=1, step=1)
    if bookno not in st.session_state.borrowed:
        st.warning("Book not found in borrowed list.")
        return
    borrowed_count = st.session_state.borrowed[bookno]
    st.write(f"Currently borrowed copies: {borrowed_count}")
    copies = st.number_input("How many copies do you want to return?", min_value=1, max_value=borrowed_count, step=1)
    if st.button("Return"):
        st.session_state.borrowed[bookno] -= copies
        st.session_state.books[bookno]['count'] += copies
        if st.session_state.borrowed[bookno] == 0:
            del st.session_state.borrowed[bookno]
        st.success(f"Returned {copies} copy/copies of '{st.session_state.books[bookno]['bookname']}' successfully.")

def delete_book():
    st.subheader("Delete Book")
    if not st.session_state.books:
        st.info("No books available to delete.")
        return
    bookno = st.number_input("Enter the book number to delete", min_value=1, step=1)
    if bookno not in st.session_state.books:
        st.warning("Book not found.")
        return
    if bookno in st.session_state.borrowed:
        st.error(f"Book '{st.session_state.books[bookno]['bookname']}' is currently borrowed and cannot be deleted.")
        return
    if st.button("Delete"):
        del st.session_state.books[bookno]
        st.success("Book deleted successfully.")

def show_borrowed():
    st.subheader("Borrowed Books")
    if not st.session_state.borrowed:
        st.info("No books have been borrowed.")
        return
    for bookno, count in st.session_state.borrowed.items():
        book = st.session_state.books[bookno]
        st.markdown(f"**Book No:** {bookno}")
        st.markdown(f" - Name: {book['bookname']}")
        st.markdown(f" - Borrowed Copies: {count}")
        st.markdown("---")

def main():
    st.title("📚 Library Management System")

    init_library()

    operation = st.sidebar.selectbox(
        "Choose an operation",
        (
            "Display available books",
            "Add books",
            "Borrow a book",
            "Return a book",
            "Delete a book",
            "Show borrowed books"
        )
    )

    if operation == "Display available books":
        display_books()
    elif operation == "Add books":
        add_book()
    elif operation == "Borrow a book":
        borrow_book()
    elif operation == "Return a book":
        return_book()
    elif operation == "Delete a book":
        delete_book()
    elif operation == "Show borrowed books":
        show_borrowed()

if __name__ == "__main__":
    main()
