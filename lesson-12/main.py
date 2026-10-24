# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

max_num = a if a > b else b
print(f"The maximum number is: {max_num}")

min_num = a if a < b else b
print(f"The minimum number is: {min_num}")

status = "Adult" if age >= 18 else "Minor"
print(f"The person is an: {status}")

weather = "Hot" if temperature >= 20 else "Cold"
print(f"The weather is: {weather}")

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(f"The user has: {access_level}")
