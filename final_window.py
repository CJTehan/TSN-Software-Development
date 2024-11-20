import tkinter as tk
from PIL import ImageTk, Image

# Make a change to a particular file, add an image
path = r"C:\Users\Conor Tehan\Documents\Software Development Bootcamp\Visual Studio Bootcamp\Software Dev 2024\Week_9_Coding\mountains.jpg"

def launch_window():
    '''
    This function creates and launches a new window
    '''
    new_window = tk.Toplevel(root)
    new_window.title('New Window')
    new_window.geometry('900x800')
    
    # Add a label to the new window
    label = tk.Label(new_window, text = 'This is a new window!')
    label.pack(pady=20)
    
    # Add a second label to the new windows with modification
    label2 = tk.Label(new_window, text='Welcome!', font = ('Arial', 24), fg = 'blue', bg = "black")
    label2.pack()
    
    # Add a button to close the new window
    close_button = tk.Button(new_window, text = 'Close', command = new_window.destroy)
    close_button.pack()
    
    def change_label_text():
        label.config(text='The the text has changed!')
    
    # Button in the new window
    change_button = tk.Button(new_window, text = 'Change Label', command = change_label_text)
    change_button.pack(pady = 10)

# Create the main window
root = tk.Tk()
root.title('Main Window')
root.geometry('900x800')
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

# Add a button to launch the new window
launch_button = tk.Button(root, text = 'Launch New Window', command = launch_window)
launch_button.pack(pady = 20)

# Start the tkinter event loop
root.mainloop()