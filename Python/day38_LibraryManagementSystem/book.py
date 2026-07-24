from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: str

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            isbn=data["isbn"],
        )
