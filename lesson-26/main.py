# Concession Stand Program

menu = {"Pizza": 3.00,
        "Nachos": 4.50,
        "Popcorn": 6.00,
        "Fries": 2.50,
        "Chips": 1.00,
        "Pretzel": 3.50,
        "Soda": 3.00,
        "Lemonade": 4.25,}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    text = f"{key}: ${value:.2f}"
    print(text.center(24))
print("------------------------")

while True:
    choice = input("What do you want to buy? ('q' to quit): ").capitalize()
    if choice.lower() == "q":
        break
    elif menu.get(choice) is not None:
        cart.append(choice)

for food in cart:
    total += menu.get(food)

for food in set(cart):
    print(f"{cart.count(food)} x {food}: ${cart.count(food) * menu[food]:.2f}")

print(f"Your total is: {total}")
