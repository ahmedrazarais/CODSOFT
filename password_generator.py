import tkinter as tk
import random

# Function to generate password
def generate_password():
    # Get the length of the password from the entry widget
    length = int(entry_length.get())
    # Define the characters to be used in the password
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special = "!@#$%^&*()_+.,/;"
    all_characters = upper + lower + numbers + special
    # Generate the password using random.sample
    password = "".join(random.sample(all_characters, length))
    # Display the generated password in the label widget
    label_password.config(text=f"Generated Password is : {password}")

# Create a Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create a label for instructions
label_instructions = tk.Label(root, text="Enter Length OF Password:")
label_instructions.pack()

# Create an entry widget for password length
entry_length = tk.Entry(root)
entry_length.pack()

# Create a button to generate password
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack()

# Create a label to display generated password
label_password = tk.Label(root, text="")
label_password.pack()

# Run the Tkinter event loop
root.mainloop()
