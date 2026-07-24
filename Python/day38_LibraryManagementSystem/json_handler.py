import json
from pathlib import Path


def save_books(filename, books):
    path = Path(filename)
    with path.open("w", encoding="utf-8") as file:
        json.dump(books, file, indent=2)


def load_books(filename):
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"No saved file found: {filename}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
