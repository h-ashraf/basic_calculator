import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Basic Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=16, borderwidth=3, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Global variable to store the current expression
expression = ""

# Function to update the expression in the entry widget
def button_click(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(tk.END, expression)  # Update with the new expression

# Function to clear the entry widget
def button_clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Function to evaluate the expression and show the result
def button_equal():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)  # Display the result
        expression = result  # Update the expression to the result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Handle errors (e.g., division by zero)

# Define the calculator buttons and layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), 
                  command=button_equal).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), 
                  command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), 
          command=button_clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='we')

# Start the GUI event loop
root.mainloop()