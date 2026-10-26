import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2","3","4","5","6","J","Q","K","A"]

print(random.randint(low, high))
print(random.random())
print(random.choice(options))
print(random.shuffle(cards))
