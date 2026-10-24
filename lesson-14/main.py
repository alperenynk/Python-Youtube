# Indexing = Accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])  # Accessing the first character
print(credit_number[5])  # Accessing the sixth character
print(credit_number[-1])  # Accessing the last character
print(credit_number[-4])  # Accessing the fourth character from the end
print(credit_number[:4])  # Accessing the first four characters -> 1234
print(credit_number[5:9])  # Accessing characters from index 5 to 8 -> 5678
print(credit_number[10:14])  # Accessing characters from index 10 to 13 -> 9012
print(credit_number[15:19])  # Accessing characters from index 15 to 18 -> 3456
print(credit_number[::5])  # Accessing every 5th character -> 1-1-4
print(credit_number[::-1])  # Reversing the string -> 6543-2109-8765-4321
