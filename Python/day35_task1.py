class Book:
    def __init__(self,Book_ID,Name,Author,Price,Filename="library.txt"):
        self.Book_ID = Book_ID
        self.Name = Name
        self.Author = Author
        self.Price = Price
        self.Filename = Filename

    def display(self):
        books = []
        print("Book ID :",self.Book_ID)
        print("Name :",self.Name)
        print("Author :",self.Author)
        print("Price :",self.Price)
        details = f"{self.Book_ID} | {self.Name}|{self.Author}|{self.Price}"
        books.append(details)


v = [
    Book("d24","Albert","Hemanth",450),
    Book("D25","BB","James",500)]
for v1 in v:

    v1.display()
    
