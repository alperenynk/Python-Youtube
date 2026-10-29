# Rock Paper Scissors Game

import random

options = ("rock", "paper", "scissors")
computer_score = 0
user_score = 0

print("Welcome to Rock Paper Scissors Game")
print("-----------------------------------")
while True:
    choice = input("Rock Paper or Scissors ('q' to quit): ").lower()

    if choice == "q":
        break
    if choice not in options:
        print("Invalid choice. Please try again.")
        continue
    computer = random.choice(options)
    if ((choice == "rock" and computer == "scissors") or 
        (choice == "paper" and computer == "rock") or 
        (choice == "scissors" and computer == "paper")):
        print("You win this round.")
        user_score += 1
    elif (choice == computer):
        print("Draw.")
    else:
        print("You lose this round.")
        computer_score += 1
    print("Computer:", computer)
    print("-----------------------------------")
if (user_score < computer_score):
    print("You lost the game :(")
elif (user_score == computer_score):
    print("Draw")
else:
    print("You won the game :)")
print("Computer Score: ", computer_score)
print("Your Score: ", user_score)
