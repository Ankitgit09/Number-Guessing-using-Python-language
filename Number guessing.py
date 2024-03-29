import random
import tkinter as tk

def check_guess():
    """Checks the user's guess and updates the label with the result."""
    guess = int(guess_entry.get())
    if guess < number:
        result_label.config(text=f"Too low! Try again.")
    elif guess > number:
        result_label.config(text=f"Too high! Try again.")
    else:
        result_label.config(text=f"Congratulations! You guessed the number {number}.")
        guess_entry.config(state="disabled")
        play_again_button.config(state="normal")

def play_again():
    """Resets the game to its initial state."""
    global number
    number = random.randint(1, 100)
    guess_entry.config(state="normal")
    result_label.config(text="")
    play_again_button.config(state="active")
    guess_entry.delete(0, tk.END)
    guess_entry.focus()

# Initialize the game variables
number = random.randint(1, 100)
guess_entry = 50

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create the label, entry, and button for the user's guess
guess_label = tk.Label(root, text="Enter your guess:")
guess_label.pack()
guess_entry = tk.Entry(root, width=50, font=("Arial", 24), justify="center")
guess_entry.pack()
guess_entry.focus()
check_button = tk.Button(root, text="Check", font=("Arial", 24), command=check_guess)
check_button.pack()

# Create the label for the result
result_label = tk.Label(root, text="", font=("Arial", 24))
result_label.pack()

# Create the button for playing again
play_again_button = tk.Button(root, text="Play Again", font=("Arial", 14), state="active", command=play_again)
play_again_button.pack()

# Start the Tkinter event loop
root.mainloop()


