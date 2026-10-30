# List Comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)

# -----------

# triples = []
# for x in range(1, 11):
#     triples.append(x * 3)

# triples = [x * 3 for x in range(1, 11)]
# print(triples)

# -----------

# numbers = [1,-2,3,-4,5,-6,-7,8]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 != 0]
# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)
