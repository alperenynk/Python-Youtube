# Python Writing Files (.txt, .json, .csv)

import json
import csv

# file_path = "lesson-60/output.txt"
# txt_data = "I like pizza!"
# try:
#     with open(file=file_path, mode="x") as file:
#         file.write(txt_data)
#         print(f"txt file created: '{file_path}'.")
# except FileExistsError:
#     print(f"File '{file_path}' already exists.")

# file_path = "lesson-60/output.txt"
# employees = ["Euegene", "Squidward", "Patrick", "SpongeBob"]
# try:
#     with open(file=file_path, mode="x") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file created: '{file_path}'.")
# except FileExistsError:
#     print(f"File '{file_path}' already exists.")

# file_path = "lesson-60/output.json"
# employee = {
#     "name": "SpongeBob",
#     "age": 30,
#     "job": "Cook"
# }
# try: 
#     with open(file=file_path, mode="w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file created: '{file_path}'.")
# except FileExistsError:
#     print(f"File '{file_path}' already exists.")

file_path = "lesson-60/output.csv"
employees = [["Name", "Age", "Job"], 
             ["SpongeBob", 30, "Cook"], 
             ["Patrick", 25, "Student"], 
             ["Squidward", 40, "Cashier"]]
try: 
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file created: '{file_path}'.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")
