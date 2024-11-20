import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def launch_window():
    """
    This function creates and launches a window
    """
    new_window = tk.Toplevel(root) # Create a new window
    new_window.title("New Window") # Set the window title
    new_window.geometry("900x800") # Set the window size

    # Add a label to the new window
    label = tk.Label(new_window, text = "This is a new window!", font =("Arial", 16))
    label.config(fg="blue")
    label.pack(pady = 20)
    label.pack()

    label2 = tk.Label(new_window, text = "Welcome to your new window!", font =("Times New Roman", 14))
    label2.config(fg="green")
    label2.pack(pady = 25)

    
    image = Image.open("welcome.jpg")
    image = ImageTk.PhotoImage(image)
    
    image_label = tk.Label(root, image=image)
    image_label.pack()

    # Add a button to close a new window
    close_button = tk.Button(new_window, text = "Close", command = new_window.destroy)
    close_button.pack()

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.title("900x800")


# Set the size of the main window explicitly
root.minsize(900, 800)
root.maxsize(900, 800)

# Add a button to launch the new window
launch_button = tk.Button(root, text = "Launch new Window", command = launch_window)
launch_button.pack(pady = 20)

root.mainloop()