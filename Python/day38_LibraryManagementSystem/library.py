import json

from Python.LibraryManagementSystem.book import Book
from Python.LibraryManagementSystem.json_handler import load_books, save_books


class Library:
    def __init__(self, filename="library_books.json"):
        self.books = []
        self.filename = filename

    def add_book(self):
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()

        while True:
            try:
                year = int(input("Enter publication year: ").strip())
                break
            except ValueError:
                print("Year must be a valid number.")

        isbn = input("Enter ISBN: ").strip()

        if not title or not author or not isbn:
            print("Title, author, and ISBN cannot be empty.")
            return

        book = Book(title=title, author=author, year=year, isbn=isbn)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def view_books(self):
        if not self.books:
            print("No books found in the library.")
            return

        print("\nLibrary Books:")
        for i, book in enumerate(self.books, start=1):
            print(
                f"{i}. Title: {book.title} | Author: {book.author} | Year: {book.year} | ISBN: {book.isbn}"
            )

    def search_book(self):
        keyword = input("Enter title, author, or ISBN to search: ").strip().lower()
        if not keyword:
            print("Search term cannot be empty.")
            return

        found_books = [
            book
            for book in self.books
            if keyword in book.title.lower()
            or keyword in book.author.lower()
            or keyword in book.isbn.lower()
        ]

        if not found_books:
            print("No matching book found.")
            return

        print("\nSearch Results:")
        for book in found_books:
            print(
                f"Title: {book.title} | Author: {book.author} | Year: {book.year} | ISBN: {book.isbn}"
            )

    def save_to_json(self):
        try:
            save_books(self.filename, [book.to_dict() for book in self.books])
            print(f"Books saved to {self.filename}.")
        except Exception as error:
            print(f"Error saving data: {error}")

    def load_from_json(self):
        try:
            data = load_books(self.filename)
            self.books = [Book.from_dict(item) for item in data]
            print(f"Books loaded from {self.filename}.")
        except FileNotFoundError:
            print("No saved library file found.")
        except json.JSONDecodeError:
            print("Invalid JSON file.")
        except Exception as error:
            print(f"Error loading data: {error}")
