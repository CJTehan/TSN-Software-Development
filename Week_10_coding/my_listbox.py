import tkinter as tk

def show_selection():
    """
    Displays the selected item from the listbox
    """
    
    selection = lb.curselection()
    if selection:
        for i in selection:
            print(lb.get(i))
    else:
            print("No item selected")

# Create the main window
window = tk.Tk()
window.title("My Listbox")

# Create a listbox with specified dimensions (no items yet)
lb = tk.Listbox(window, height = 6, width = 20) # Set the height and width
lb.pack(pady = 20)


# Insert items into Listbox AFTER the button is clicked
def add_items():
    
    lb.insert(0, "Labrador")
    lb.insert(1, "Retriever")
    lb.insert(2, "German Shepherd")
    lb.insert(3, "Yorkie")
    

# Create a button to show the selection
show_button = tk.Button(window, text = "Show Selection", command = add_items)
show_button.pack()

window.mainloop()