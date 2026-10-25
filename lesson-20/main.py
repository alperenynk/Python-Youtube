# Nested Loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

for _ in range(3):
    for x in range(1, 10):
        print(x, end="")
    print()

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")
for _ in range(rows):
    for _ in range(columns):
        print(symbol, end="")
    print()
