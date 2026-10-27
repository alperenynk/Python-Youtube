# Python Number Guessing Game

import random
number = random.randint(1, 100)
guess_time = 0
guess = 0

print("Python Number Guessing Game")

while guess != number:
    guess = int(input("Guess between 1 - 100: "))
    if (100 < guess or 0 >= guess):
        print("The number should be between 1 - 100")
    else:
        guess_time += 1
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
    
print(f"Congratulations! You guessed the number in {guess_time} try!")
