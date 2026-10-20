# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Alperen"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)  # Convert float to int
age = float(age)  # Convert int to float
age = str(age)  # Convert float to str
name = bool(name)  # Convert str to bool
print(name)
