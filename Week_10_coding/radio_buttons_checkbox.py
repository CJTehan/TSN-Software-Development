import tkinter as tk
from tkinter import messagebox

def show_checkbox():
    """
    Displaying a messagebox with checkbox options to go with the radio buttons
    """
    selected_team = [team for i, team in enumerate(teams) if checkbox_vars[1].get()]
    if show_checkbox:
        message = "You chose:\n" + "\n".join(selected_team)
    else:
        message = "You didn't select a team!"
    
    messagebox.showinfo("Selected team",  message)


# Create the main window
window = tk.Tk()
window.title("Checkboxes and Radio Buttons")


# --- Checkboxes ---
teams = ["Sheffield United", "Sheffield Wednesday", "Barnsley"]
checkbox_vars = [tk.BooleanVar() for __ in teams]

tk.Label(window, text = "Select your team:").pack(anchor= tk.W)

for i, team in enumerate(teams):
    tk.Checkbutton(window, text = team, variable = checkbox_vars[i]).pack(anchor = tk.W)

# Create a StringVar to store the selected value
selected_option = tk.StringVar(value = "Home Kit") # Setting the default selection

# Create a label
tk.Label(window, text = "Select a kit:").pack(anchor = tk.W)

# Create radio buttons
tk.Radiobutton(window, text = "Home Kit", variable = selected_option, value = "Home Kit").pack(anchor = tk.W)
tk.Radiobutton(window, text = "Away Kit", variable = selected_option, value = "Away Kit").pack(anchor = tk.W)
tk.Radiobutton(window, text = "Third Kit", variable = selected_option, value = "Third Kit").pack(anchor = tk.W)

# Function to show the selected value in a messagebox
def show_selected():
    messagebox.showinfo("Selected Option", f"You selected: {selected_option.get()}")

# Create a button to display the selected value
show_button = tk.Button(window, text = "Show Selected kit", command = show_selected)
show_button.pack(pady = 20)

# Create a button to show the selected check box
show_option_button = tk.Button(window, text = "Show Selected Team", command = show_checkbox)
show_option_button.pack(pady = 20)


window.mainloop()