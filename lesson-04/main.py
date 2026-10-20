# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))
age += 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

# Exercise 1: Rectangle Area Calc
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}cm²")

# Exercise 2: Shopping Cart Program
item = input("What item would you like to purchase?: ")
price = float(input(f"What is the price of {item}?: "))
quantity = int(input(f"How many {item} would you like to buy?: "))
total = price * quantity
print(f"You have purchased {quantity} {item}(s)")
print(f"The total cost is: ${total}")