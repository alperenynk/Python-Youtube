# Function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old.")
    print("Happy birthday to you")
    print()

happy_birthday("Alperen", 21)
happy_birthday("Selma", 18)

# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(4, 2))
print(subtract(4, 2))
print(multiply(4, 2))
print(divide(4, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bro", "code")
print(full_name)
