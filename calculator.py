# Import the Tkinter module
import tkinter as tk

# Create a class for the calculator
class Calculator:
    # Initialize the calculator
    def __init__(self, root):
        # Store the root window
        self.root = root
        # Set the title of the window
        self.root.title("Simple Calculator")
        # Create a StringVar to store the input expression
        self.expression = tk.StringVar()
        # Create a text entry widget to display the expression
        self.entry = tk.Entry(root, textvariable=self.expression, font=('Arial', 18))
        # Set the grid layout for the text entry widget
        self.entry.grid(row=0, column=0, columnspan=4)
        # Call the method to create buttons
        self.create_buttons()

    # Method to handle button clicks
    def button_click(self, value):
        # Get the current expression
        current_expression = self.expression.get()
        # Append the clicked button's value to the expression
        self.expression.set(current_expression + value)

    # Method to evaluate the expression and display the result
    def evaluate(self):
        try:
            # Evaluate the expression
            result = str(eval(self.expression.get()))
            # Display the result in the entry widget
            self.expression.set(result)
        except:
            # If an error occurs during evaluation, display "Error"
            self.expression.set("Error")

    # Method to clear the expression
    def clear(self):
        # Clear the expression
        self.expression.set("")

    # Method to create buttons
    def create_buttons(self):
        # Define button labels
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        # Loop to create buttons
        for (text, row, column) in buttons:
            # Create a button with the specified text
            button = tk.Button(self.root, text=text, font=('Arial', 14), padx=10, pady=10,
                               command=lambda value=text: self.button_click(value))
            # Set the grid layout for the button
            button.grid(row=row, column=column, padx=5, pady=5)
        # Create a button to clear the expression
        clear_button = tk.Button(self.root, text='C', font=('Arial', 14), padx=10, pady=10,
                                 command=self.clear)
        # Set the grid layout for the clear button
        clear_button.grid(row=0, column=4, padx=5, pady=5)
        # Create a button to evaluate the expression
        equals_button = tk.Button(self.root, text='=', font=('Arial', 14), padx=10, pady=10,
                                  command=self.evaluate)
        # Set the grid layout for the equals button
        equals_button.grid(row=4, column=4, padx=5, pady=5)

# Create the main function
def main():
    # Create a Tkinter root window
    root = tk.Tk()
    # Create an instance of the Calculator class
    calculator = Calculator(root)
    # Run the Tkinter event loop
    root.mainloop()

# Call the main function
if __name__ == "__main__":
    main()
