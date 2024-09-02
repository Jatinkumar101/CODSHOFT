import random
import string
from tkinter import *

# Create the main window
root = Tk()
root.title("Password Generator")
root.config(bg="#dcd1d7")

# Function to generate a random password
def generate_password():

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Get user selections for character sets
    include_uppercase = var_uppercase.get()
    include_numbers = var_numbers.get()
    include_symbols = var_symbols.get()

    # Combine character sets based on selections
    char_set = ""
    if include_uppercase:
        char_set += uppercase
    if include_numbers:
        char_set += numbers
    if include_symbols:
        char_set += symbols
    char_set += lowercase

    # Get password length from entry field
    password_length = int(entry_length.get())

    # Generate random password
    password = ''.join(random.sample(char_set, password_length))

    # Display generated password
    entry_password.delete(0, END)
    entry_password.insert(0, password)

# Getting password length entry
label_length = Label(root, bg="#dcd1d7", text="Password Length:")
label_length.grid(row=0, column=0, padx=5, pady=5)

entry_length = Entry(root, bg="#dcd1d7", width=10, font=( 12))
entry_length.insert(0, 8)               # Set default length to 8
entry_length.grid(row=0, column=1, padx=5, pady=5)

# Asking whether to include uppercases
label_uppercase = Label(root, bg="#dcd1d7", text="Include Uppercase Letters:")
label_uppercase.grid(row=1, column=0, padx=5, pady=5)

var_uppercase = IntVar()
check_uppercase = Checkbutton(root, bg="#dcd1d7", variable=var_uppercase, onvalue=1, offvalue=0)
check_uppercase.grid(row=1, column=1, padx=5, pady=5)

# Asking whether to include Numbers
label_numbers = Label(root, bg="#dcd1d7", text="Include Numbers:")
label_numbers.grid(row=2, column=0, padx=5, pady=5)

var_numbers = IntVar()
check_numbers = Checkbutton(root, bg="#dcd1d7", variable=var_numbers, onvalue=1, offvalue=0)
check_numbers.grid(row=2, column=1, padx=5, pady=5)

# Asking whether to include Symbols
label_symbols = Label(root, bg="#dcd1d7", text="Include Symbols:")
label_symbols.grid(row=3, column=0, padx=5, pady=5)

var_symbols = IntVar()
check_symbols = Checkbutton(root, bg="#dcd1d7", variable=var_symbols, onvalue=1, offvalue=0)
check_symbols.grid(row=3, column=1, padx=5, pady=5)

# Showing the generated password
label_password = Label(root, bg="#dcd1d7", text="Generated Password:")
label_password.grid(row=4, column=0, padx=5, pady=5)

entry_password = Entry(root, bg="#dcd1d7", width=20, font=("Calibri", 14))
entry_password.grid(row=4, column=1, padx=5, pady=5)

# Generate button
button_generate = Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=5, columnspan=2, padx=5, pady=5)

root.mainloop()
