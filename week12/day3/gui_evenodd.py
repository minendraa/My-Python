import tkinter as tk
from tkinter import messagebox

# Initialize state variables
numbers = []

def submit_number():
    try:
        num = int(entry.get())
        numbers.append(num)
        entry.delete(0, tk.END)

        status_label.config(text=f"{len(numbers)} number(s) entered.")

        if len(numbers) == 10:
            # Count even and odd
            even = sum(1 for n in numbers if n % 2 == 0)
            odd = 10 - even
            result_label.config(text=f"{even} are even and {odd} are odd.")
            submit_button.config(state="disabled")
            entry.config(state="disabled")
        else:
            result_label.config(text="")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def reset_game():
    numbers.clear()
    entry.config(state="normal")
    submit_button.config(state="normal")
    entry.delete(0, tk.END)
    result_label.config(text="")
    status_label.config(text="Enter number 1 of 10")

# GUI setup
root = tk.Tk()
root.title("Even/Odd Counter")
root.geometry("400x250")

prompt_label = tk.Label(root, text="Enter one number at a time:")
prompt_label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit Number", command=submit_number)
submit_button.pack(pady=10)

status_label = tk.Label(root, text="Enter number 1 of 10")
status_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack(pady=5)

root.mainloop()
