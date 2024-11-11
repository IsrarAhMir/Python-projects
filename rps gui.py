import tkinter as tk
import random

user_wins = 0
computer_wins = 0
ties = 0


options = ["rock", "paper", "scissors"]

def play(user_input):
    global user_wins, computer_wins, ties

    computer_pick = random.choice(options)
    result_text.set(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        ties += 1
        result_text.set(result_text.get() + " It's a tie!")
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        user_wins += 1
        result_text.set(result_text.get() + " You win!")
    else:
        computer_wins += 1
        result_text.set(result_text.get() + " Computer wins!")

   
    score_text.set(f"Your Wins: {user_wins} | Computer Wins: {computer_wins} | Ties: {ties}")


window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x300")

# Labels and text variables for displaying results
result_text = tk.StringVar()
score_text = tk.StringVar(value="Your Wins: 0 | Computer Wins: 0 | Ties: 0")

result_label = tk.Label(window, textvariable=result_text, font=("Helvetica", 14))
score_label = tk.Label(window, textvariable=score_text, font=("Helvetica", 14))

# Buttons for game options
rock = tk.Button(window, text="ROCK", command=lambda: play("rock"), width=10, font=("Helvetica", 12))
paper = tk.Button(window, text="PAPER", command=lambda: play("paper"), width=10, font=("Helvetica", 12))
scissor = tk.Button(window, text="SCISSORS", command=lambda: play("scissors"), width=10, font=("Helvetica", 12))

# Button to quit the game
quit_button = tk.Button(window, text="QUIT", command=window.quit, width=10, font=("Helvetica", 12))


result_label.pack(pady=10)
rock.pack(pady=5)
paper.pack(pady=5)
scissor.pack(pady=5)
score_label.pack(pady=10)
quit_button.pack(pady=10)

# Run the main event loop
window.mainloop()
