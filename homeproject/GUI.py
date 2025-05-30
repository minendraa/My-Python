from tkinter import *
from tkinter import messagebox, simpledialog, ttk
from datetime import datetime

# Data storage
bookname = []
author = []
readstatus = []
date = []

# Add book function
def add_book():
    nameofbook = simpledialog.askstring("Book Name", "Enter the name of the book:")
    if not nameofbook:
        return
    nameofauthor = simpledialog.askstring("Author Name", "Enter the name of the author:")
    if not nameofauthor:
        return
    status = messagebox.askquestion("Read Status", "Have you read this book?")

    bookname.append(nameofbook.capitalize())
    author.append(nameofauthor.capitalize())
    date.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    readstatus.append("Read" if status == "yes" else "Not read yet...")

    messagebox.showinfo("Success", f"'{nameofbook}' has been added to your library.")
    update_listbox()

# Remove book function
def remove_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a book to remove.")
        return
    index = selected[0]
    book_removed = bookname[index]
    del bookname[index]
    del author[index]
    del readstatus[index]
    del date[index]
    messagebox.showinfo("Removed", f"'{book_removed}' removed successfully.")
    update_listbox()

# Update display
def update_listbox():
    listbox.delete(0, END)
    for i in range(len(bookname)):
        entry = f"{i+1}. {bookname[i]} by {author[i]} [{readstatus[i]}] on {date[i]}"
        listbox.insert(END, entry)

# Quit application
def quit_app():
    root.destroy()

# GUI Setup
root = Tk()
root.title("📚 Personal Book Library Manager")
root.geometry("700x400")
root.config(padx=10, pady=10)

# Buttons
Button(root, text="Add Book", command=add_book, width=15).grid(row=0, column=0, padx=5, pady=5)
Button(root, text="Remove Book", command=remove_book, width=15).grid(row=0, column=1, padx=5, pady=5)
Button(root, text="Quit", command=quit_app, width=15).grid(row=0, column=2, padx=5, pady=5)

# Listbox with scrollbar
frame = Frame(root)
frame.grid(row=1, column=0, columnspan=3, pady=10)
scrollbar = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, width=90, height=15, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH)

root.mainloop()
