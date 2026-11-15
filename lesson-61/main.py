# Python Reading Files (.txt, .json, .csv)

import json
import csv

# file_path = "lesson-61/data.txt"
# try:
#     with open(file=file_path, mode="r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")
# except PermissionError:
#     print(f"Permission denied to read file '{file_path}'.")

# file_path = "lesson-61/data.json"
# try:
#     with open(file=file_path, mode="r") as file:
#         content = json.load(file)
#         print(content["name"])
# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")
# except PermissionError:
#     print(f"Permission denied to read file '{file_path}'.")

file_path = "lesson-61/data.csv"
try:
    with open(file=file_path, mode="r", newline="") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except PermissionError:
    print(f"Permission denied to read file '{file_path}'.")
