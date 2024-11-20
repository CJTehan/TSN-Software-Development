import tkinter as tk
from tkinter import messagebox

def show_info_message():
    messagebox.showinfo("Information", "This is an information message!")

def show_warning_message():
    messagebox.showwarning("Warning", "This is a warning message!")

def show_error_message():
    messagebox.showerror("Error", "This is an error message!")

# Create the main window
root = tk.Tk()
root.title("Message Boxes")
root.geometry("600x400")

# Create buttons to trigger different message boxes
info_button = tk.Button(root, text = "Show Info", command = show_info_message)
info_button.pack(pady = 10)

warning_button = tk.Button(root, text = "Show Warning", command = show_warning_message)
warning_button.pack(pady = 10)

error_button = tk.Button(root, text = "Show Error", command = show_error_message)
error_button.pack(pady = 10)

root.mainloop()