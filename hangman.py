# Run the loop
import random
import tkinter as tk

# --- Constants ---
MAX_ATTEMPTS = 6
CATEGORIES = {
    "Animals": ["Porcupine", "Alligator", "Wolf", "Turtle", "Lion", "Koala", "Capybara", "Grizzly Bear", "Badger"],
    "Countries": ["France", "England", "Germany", "Spain", "Italy", "Colombia", "Venezuela", "Ireland", "Norway", "United States"],
    "Movies": ["Interstellar", "Pulp Fiction", "Harry Potter", "Zodiac", "Se7ven", "Lord of the rings", "Shawshank Redemption"],
    "Sports": ["Football", "Cricket", "Rugby", "Tennis", "Squash", "Bouldering", "Skiing", "Snowboarding"],
    "TV Shows": ["Friends", "The Walking Dead", "Game of Thrones", "The Simpsons", "Family guy", "Mindhunter", "House", "Breaking Bad"]
    }

# --- Functions --- 
def get_word():
    """
    Gets a random word from the chosen category
    """
    category = category_var.get()
    word = random.choice(CATEGORIES[category])
    return word.upper()

def start_game():
    """
    Initialises the game
    """
    global word, attempts_remaining, guessed_letters
    word = get_word()
    attempts_remaining = MAX_ATTEMPTS
    guessed_letters = []
    update_display()
    guess_entry.config(state = "normal")
    guess_button.config(state = "normal")
    hint_button.config(state = "normal")

def update_display():
    """
    Updates the display with the current game state 
    """
    hidden_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    word_label.config(text = hidden_word)
    attempt_label.config(text = f"Attempts remaining: {attempts_remaining}")
    canvas.delete("all")
    draw_hangman()

def guess_letter():
    """
    Handles the player's guess
    """
    global attempts_remaining
    guess = guess_entry.get().upper()
    guess_entry.delete(0, tk.END)

    if not guess.isalpha() or len(guess) != 1:
        message_label.config(text = "Invalid input, must use a single letter")
        return
    
    if guess in guessed_letters:
        message_label.config(text = "Letter guessed already, pick another letter")
        return
    
    guessed_letters.append(guess)

    if guess not in word:
        attempts_remaining -= 1
        message_label.config(text = "Incorrect Guess")
    else:
        message_label.config(text = "Correct Guess")

    update_display()
    check_game_over()

def give_hint():
    """
    Provides a hint to the player
    """
    global attempts_remaining
    if attempts_remaining > 1:
        attempts_remaining -= 1
        while True:
            hint_letter = random.choice(word)
            if hint_letter not in guessed_letters:
                guessed_letters.append(hint_letter)
                break
        message_label.config(text = f"Hint: The word contains the letter \"{hint_letter}\"")
        update_display()
        check_game_over()
    else:
        message_label.config(text = "Not enough attempts for a hint")
        
def check_game_over():
    """
    Checks to see if the game is over (win or lose)
    """
    global attempts_remaining
    if all(letter in guessed_letters for letter in word):
        message_label.config(text = "You Win!", fg = "red")
        disable_input()
    elif attempts_remaining == 0: # Check for losing condition
        message_label.config(text = f"You Lose! The word was {word}", fg = "blue")

def disable_input():
    """Disables the input fields"""
    guess_entry.config(state = "disabled")
    guess_button.config(state = "disabled")
    hint_button.config(state = "disabled")

def draw_hangman():
    """
    Draws the stick figure drawing to display on the canvas
    """
    if attempts_remaining <= 5:
       canvas.create_line(50, 150, 150, 150) # Base
    if attempts_remaining <= 4:
        canvas.create_line(100, 150, 100, 50) # Upright
    if attempts_remaining <= 3:
        canvas.create_line(100, 50, 150, 50) # Top
    if attempts_remaining <= 2:
        canvas.create_line(150, 50, 150, 70) # Noose
    if attempts_remaining <= 1:
        canvas.create_oval(140, 70, 160, 90) # Head
    if attempts_remaining == 0:
        canvas.create_line(150, 90, 150, 120) # Body
        canvas.create_line(150, 100, 130, 110) # Left Arm
        canvas.create_line(150, 100, 170, 100) # Right Arm
        canvas.create_line(150, 120, 130, 140) # Left Leg
        canvas.create_line(150, 120, 170, 140) # Right Leg


# --- GUI Setup ---
window =  tk.Tk()
window.title("Hangman")
window.geometry("900x800")

# Categories selection
category_var = tk.StringVar(value = "Animals")
category_label = tk.Label(window, text = "Category")
category_option = tk.OptionMenu(window, category_var, *CATEGORIES.keys())

# Word display
word_label = tk.Label(window, text = "_ _ _ _ _ ", font = ("Arial", 24))

# Attempts display
attempt_label = tk.Label(window, text = f"Attempts remaining: {MAX_ATTEMPTS}")

# Canvas for Hangman figure
canvas = tk.Canvas(window, width = 200, height = 200)

# Guess input
guess_entry = tk.Entry(window, state = "disabled")
guess_button = tk.Button(window, text = "Guess", command = guess_letter, state = "normal")

# Hint Button
hint_button = tk.Button(window, text = "Click for a hint", command = give_hint, state = "normal")

# Message Label
message_label = tk.Label(window, text = "")

# Start Button
start_button = tk.Button(window, text = "Start Game", command = start_game, state = "normal")

# --- Layout (using grid) ---
category_label.grid(row = 0, column = 0, padx = 5, pady = 5)
category_option.grid(row = 0, column = 1, padx = 5, pady = 5)
start_button.grid(row = 0, column = 2, padx = 5, pady = 5)
word_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
attempt_label.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 5)
canvas.grid(row = 3, column = 0, columnspan = 3, padx = 5, pady = 5)
guess_entry.grid(row = 4, column = 0, padx = 5, pady = 5)
guess_button.grid(row = 4, column = 2, padx = 5, pady = 5)
message_label.grid(row = 5, column = 0, columnspan = 3, padx = 5, pady = 5)

# Run the loop
window.mainloop()