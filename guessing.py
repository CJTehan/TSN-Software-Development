import random
import tkinter as tk
from tkinter import messagebox

# Function to check the guess
def check_guess():
    global guesses_left
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 100:
            messagebox.showerror("Invalid input", "Please enter a number between 1 and 100.")
            return

        guesses_left -= 1
        if guess < number:
            result_label.config(text=f"Too low! {guesses_left} guesses left.")
        elif guess > number:
            result_label.config(text=f"Too high! {guesses_left} guesses left.")
        else:
            result_label.config(text="Congratulations! You guessed the number.")
            entry.config(state="disabled")
            check_button.config(state="disabled")

        if guesses_left == 0 and guess != number:
            result_label.config(text=f"Game over! The number was {number}.")
            entry.config(state="disabled")
            check_button.config(state="disabled")
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

        # Generate a secret number
number = random.randint(1, 100)
guesses_left = 7

# Create the user interface
window = tk.Tk()
window.title("Guessing Game")

# Label for instructions
label = tk.Label(window, text="I'm thinking of a number between 1 and 100.")
label.pack(pady=10)

# Entry field for the guess
entry = tk.Entry(window)
entry.pack(pady=5)

# Check button
check_button = tk.Button(window, text="Check", command=check_guess)
check_button.pack(pady=5)

# Result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the Tkinter loop
window.mainloop()

