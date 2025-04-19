# Import Random
import random
import tkinter as tk
from tkinter import messagebox

# Create variable to track number of guesses left
def remaining_guesses():
    """
    Checks the user's guess against the secret number
    """
    # Using global to keep the guess to count down
    global guesses_left
    try:
        user_guess = int(entry.get())
        if user_guess < 1 or user_guess > 100:
            messagebox.showerror("Invalid", "Your guess must be between 1 and 100")
            return
        
        guesses_left -= 1
        if guesses_left < number:
            result_label.config(text = f"Too Low, try higher you have {guesses_left} guesses left")
        elif guesses_left > number:
            result_label.config(text = f"Too High! try lower you have {guesses_left} guesses left")  
        else:
            result_label.config(text = "Congratulations you guessed the right number!")
            entry.config(state = "disabled")
            check_button.config(state = "disabled")

        if guesses_left == 0 and user_guess != number:
            result_label.config(text = f"You're out of lives, Game over, The number was {number}")
            entry.config(state = "disabled")
            check_button.config(state = "disabled")
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

# generate a rand number between 1 and 100
number = random.randint(1, 100)
guesses_left = 7

# Create the main window
window = tk.Tk()
window.title("Guessing Game")

# entry field
entry = tk.Entry(window)
entry.pack(pady = 20)

#check button
check_button = tk.Button(window, text = "Is your guess correct?", command = remaining_guesses)
check_button.pack(pady = 20)

#result label
result_label = tk.Label(window, text = "Your result")
result_label.pack(pady = 20)

# Run the loop
window.mainloop()