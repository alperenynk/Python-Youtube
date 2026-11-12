# Exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, ValueError, TypeError)
#             1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception:
    print("An unexpected error occurred.")
finally:
    print("Do some cleanup here.")
