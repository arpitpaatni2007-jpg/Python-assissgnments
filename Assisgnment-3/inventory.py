import json
import logging
from pathlib import Path
from book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def __init__(self, filepath="catalog.json"):
        self.filepath = Path(filepath)
        self.books = []
        self.load()

    def save(self):
        try:
            data = [b.to_dict() for b in self.books]
            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=4)
            logging.info("Catalog saved successfully.")
        except Exception as e:
            logging.error(f"Error saving catalog: {e}")

    def load(self):
        try:
            if self.filepath.exists():
                with open(self.filepath, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**item) for item in data]
                logging.info("Catalog loaded successfully.")
            else:
                self.books = []
        except Exception as e:
            logging.error(f"Error loading catalog: {e}")
            self.books = []

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Book added: {book.title}")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        if not self.books:
            print("No books available.")
            return
        
        for b in self.books:
            print(b)
