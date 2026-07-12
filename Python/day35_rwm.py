class Book:
    def __init__(self,Book_ID,Name,Author,Price,Filename="library1.txt"):
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
books = []

b = Book("DD24","Hemanth","jenny" ,389)
b1   =  Book("DD23","hinata","hyuga" ,469)

books.append(b)
books.append(b1)

for ed in books:
    with open(ed.Filename, "a+") as f:
        add = f"{ed.Book_ID}|{ed.Name}|{ed.Author}|{ed.Price}\n"
        f.write(add)

    ed.display()
    print("_" * 30)