import tkinter as tk
import random

user_wins = 0
computer_wins = 0
ties = 0 
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit.").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue
    random_number = random.randint(0,2)
    # rock: 0 , paper: 1, scissors: 2

    computer_pick =  options[random_number]
    print("computer picked", computer_pick + ".")
    
    if  user_input == "rock" and  computer_pick == "scissors":
        print("you win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick ==  "rock":
        print("you win!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("you win!")
        user_wins += 1
    
    elif  user_input == computer_pick:
        print("it's a tie!")
        ties += 1
        
    else:
        print("computer wins!")
        computer_wins += 1


print("you won ", user_wins, "times.")
print("computer won ", computer_wins, "times.")
print("Tied games:", ties)
print("Thanks for playing")
