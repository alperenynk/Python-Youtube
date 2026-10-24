# name = input("Enter your full name: ")
# length = len(name)
# findchar = name.find("o")
# findlastchar = name.rfind("o")
# nameCap = name.capitalize()
# nameUpper = name.upper()
# nameLower = name.lower()
# nameIsDigit = name.isdigit() # If string only contains digits, returns True. Otherwise, returns False.
# nameIsAlpha = name.isalpha() # If string only contains letters, returns True. Otherwise, returns False.

# print(length)
# print(findchar)
# print(findlastchar)
# print(nameCap)
# print(nameUpper)
# print(nameLower)
# print(nameIsDigit)
# print(nameIsAlpha)

# phone_number = input("Enter your phone number: ")
# phone_count = phone_number.count("-") # Counts the number of occurrences of the character "-" in the phone number.
# phone_number = phone_number.replace("-", " ") # Removes the "-" characters from the phone number.

# print(phone_count)
# print(phone_number)

# To access all str methods, you can use help(str) in the Python shell. This will display a list of all available string methods and their descriptions.

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits
username = input("Enter your username: ")
if len(username) > 12:
    print("Username must be no more than 12 characters.")
# elif " " in username:
#     print("Username must not contain spaces.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces.")
elif not username.isalpha():
    print("Username must not contain digits.")
else:
    print(f"Welcome {username}!") 
