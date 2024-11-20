import tkinter as tk
from tkinter import messagebox

def show_selection():
    """
    Displays a messagebox with the selected checkbox options
    """
    selected_options = [topping for i, topping in enumerate(toppings) if checkbox_vars[i].get()]
    if selected_options:
        message = "You selected:\n" + "\n ".join(selected_options)
    else:
        message = "You have not selected any options"

    messagebox.showinfo("Selected Options", message)

# Create the main window
window = tk.Tk()
window.title("Checkbox Example")

# --- Checkboxes ---
toppings = ["Sprinkles", "Chocolate Sauce", "Whipped Cream"]
checkbox_vars = [tk.BooleanVar() for __ in toppings]

tk.Label(window, text = "Select your toppings:").pack(anchor = tk.W)

for i, topping in enumerate(toppings):
    tk.Checkbutton(window, text = topping, variable = checkbox_vars[i]).pack(anchor = tk.W)

# --- Button to show selection ---
show_button = tk.Button(window, text = "Show Selected", command = show_selection)
show_button.pack(pady = 20)

window.mainloop()