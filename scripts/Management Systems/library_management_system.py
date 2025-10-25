"""
Library Management System

Description:
A simple command-line library system that allows users to add, view, borrow, 
and return books. Data is stored in a JSON file to maintain persistence.

Time Complexity:
- Adding a Book: O(1)
- Viewing Books: O(n)
- Borrowing/Returning a Book: O(n)

Space Complexity: O(n) - stores all books in memory.
"""

import json
import os


class Book:
    """Represents a single book in the library."""

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available


class Library:
    """Manages the collection of books and user interactions."""

    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """Load books from JSON file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Book(**b) for b in data]
        return []

    def save_books(self):
        """Save all books to JSON file."""
        with open(self.filename, "w") as f:
            json.dump([b.__dict__ for b in self.books], f, indent=2)

    def add_book(self):
        """Add a new book to the library."""
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        self.books.append(Book(book_id, title, author))
        self.save_books()
        print(f"✅ Book '{title}' added successfully!")

    def view_books(self):
        """Display all books in the library."""
        print("\n📚 Library Books:")
        if not self.books:
            print("No books available in the library.")
            return
        for b in self.books:
            status = "Available" if b.available else "Borrowed"
            print(f"{b.book_id} | {b.title} | {b.author} | {status}")

    def borrow_book(self):
        """Borrow a book by entering its ID."""
        book_id = input("Enter Book ID to borrow: ")
        for b in self.books:
            if b.book_id == book_id and b.available:
                b.available = False
                self.save_books()
                print(f"📖 You borrowed '{b.title}'")
                return
        print("⚠️ Book not available or invalid ID!")

    def return_book(self):
        """Return a borrowed book by entering its ID."""
        book_id = input("Enter Book ID to return: ")
        for b in self.books:
            if b.book_id == book_id and not b.available:
                b.available = True
                self.save_books()
                print(f"📘 You returned '{b.title}'")
                return
        print("⚠️ Invalid Book ID or book was not borrowed!")


# Test cases (interactive simulation)
if __name__ == "__main__":
    library = Library()

    while True:
        print("\n--- 📚 Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            print("👋 Exiting... Thank you for using the Library System!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")
