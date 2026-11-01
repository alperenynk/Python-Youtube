# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    # Override
    def describe(self):
        super().describe()
        print(f"It is a cirlce with an area of {self.radius * self.radius * 3.14}cm^2")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = Circle("red", filled=True, radius=5)
print(f"Circle: {circle.color}")
print(f"Circle: {circle.filled}")
print(f"Circle: {circle.radius}cm")
circle.describe()

square = Square(color="blue", filled=False, width=6)
print(f"Square: {square.color}")
print(f"Square: {square.filled}")
print(f"Square: {square.width}cm")
square.describe()

triangle = Triangle(color="yellow", filled=True, width=6, height=9)
print(f"Triangle: {triangle.color}")
print(f"Triangle: {triangle.filled}")
print(f"Triangle: {triangle.width}cm")
print(f"Triangle: {triangle.height}cm")
triangle.describe()
