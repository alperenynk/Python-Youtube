# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance Methods = Best for operations on instances of the class(objects)
# Static Methods = Best for utility functions that do not need access to class data
# Class Methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Alperen", 3.1)
student2 = Student("Selma", 3.05)
student3 = Student("Perihan", 2.4)
print(Student.get_count())
print(Student.get_average_gpa())
