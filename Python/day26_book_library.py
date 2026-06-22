class Book:
    def __init__(self,book_name):
        self.book_name = book_name
        

class Library:
    def __init__(self,name):
        self.name = name

book = Book("Python Programming")
library = Library(book)

print(library.name.book_name)

