# Python Banking Program

# 1. Show Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

def show_balance(balance):
    print(f"Your balance: ${balance:.2f}")

def deposit():
    amount = float(input("How much you want to deposit?: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("How much you want to withdraw?: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def main():
    balance = 0
    while True:

        print("\n     Banking Program     ")
        print("-------------------------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                break
            case _:
                print("That is not a valid choice.")
    print("Thank you! Have a nice day")

if __name__ == "__main__":
    main()
