class Book:
    def __init__(self, Book_ID, Name, Author, Price, Filename="library.txt"):
        self.Book_ID = Book_ID
        self.Name = Name
        self.Author = Author
        self.Price = Price
        self.Filename = Filename

    def display(self):
        print("Book ID :", self.Book_ID)
        print("Name :", self.Name)
        print("Author :", self.Author)
        print("Price :", self.Price)

    def Add_Book(self):
        details = f"{self.Book_ID}|{self.Name}|{self.Author}|{self.Price}"
        with open(self.Filename, "a") as file:
            file.write(details + "\n")


v = [
    Book("101", "Python", "Mosh", 500),
    Book("102", "AI Basics", "James", 450)
]

for book in v:
    book.display()
    book.Add_Book()

    