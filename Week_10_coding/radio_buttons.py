import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Radio Button Example")

# Create a StringVar to store the selected value
selected_option = tk.StringVar(value = "Option 1") # Setting the default selection

# Create a label
tk.Label(window, text = "Select an option:").pack(anchor = tk.W)

# Create radio buttons
tk.Radiobutton(window, text = "Option 1", variable = selected_option, value = "Option 1").pack(anchor = tk.W)
tk.Radiobutton(window, text = "Option 2", variable = selected_option, value = "Option 2").pack(anchor = tk.W)
tk.Radiobutton(window, text = "Option 3", variable = selected_option, value = "Option 3").pack(anchor = tk.W)

# Function to show the selected value in a messagebox
def show_selected():
    messagebox.showinfo("Selected Option", f"You selected: {selected_option.get()}")

# Create a button to display the selected value
show_button = tk.Button(window, text = "Show Selected", command = show_selected)
show_button.pack(pady = 20)

window.mainloop()