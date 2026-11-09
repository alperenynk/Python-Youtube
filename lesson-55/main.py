# Magic Methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # This method is called when we use the print() function on a Book object.
    # print(book1) will call book1.__str__() and return the string representation of the object.
    # If we don't define this method, the default string representation of the object will be returned, which is not very informative. It points to the memory location of the object.
    def __str__(self):
        return f"{self.title} by {self.author}"

    # This method is called when we use the equality operator (==) to compare two Book objects.
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # This method is called when we use the less than operator (<) to compare two Book objects.
    def __lt__(self, other):
        return self.pages < other.pages

    # This method is called when we use the greater than operator (>) to compare two Book objects.
    def __gt__(self, other):
        return self.pages > other.pages

    # This method is called when we use the addition operator (+) to add two Book objects.
    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"Invalid key: {key}. Valid keys are 'title', 'author', and 'pages'."

book1 = Book("Python Rocks!", "Jose Portilla", 159)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 295)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 195)

print(book1) # This will call the __str__ method and print "Python Rocks! by Jose Portilla"
print(book2) # This will call the __str__ method and print "The Hobbit by J.R.R. Tolkien"
print(book3) # This will call the __str__ method and print "The Lion, the Witch and the Wardrobe by C.S. Lewis"
print(book2 == book3)  # False
print(book1 < book2)   # True
print(book1 > book3)   # False
print(book1 + book2)  # 454 (159 + 295)
print("Python" in book1)  # True
print(book1["title"])  # "Python Rocks!"
