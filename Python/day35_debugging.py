class Book:
    books=[]
    def __init__(self,ID,Name,Author,price):
        self.ID = ID
        self.Name = Name
        self.Author = Author
        self.Price = price
        
    def display(self):
        print("ID :",self.ID)
        print("Name :",self.Name)
        print("Author :",self.Author)
        print("Price :",self.Price)

    

book = Book(101, "Python", "Mosh", 500)

books = [book]

for b in books:
    b.display()

    """the error was at there not kept class and name 
    , __init__ method , display method and books = square brackets
      in book then it we be in list form"""