class Book:
    def __init__(self):
        self.borrowed_books = open("borrowed.txt", "r")
        self.books = open("books.txt", "r")

    def specific_book_available(self, book):
        if book in self.books:
            if book in self.borrowed_books:
                return "This book isn't available."
            return "This book is available and you can borrow it."
        return "There is no such book."

    @property
    def current_available_books(self):
        available_books = []
        for book in self.books.readlines():
            available_books.append(book)
        if not available_books:
            return "There aren't any available books."
        return available_books

    def current_return_books(self, output):
        for book in self.books.readlines():
            if book not in self.borrowed_books:
                output.append(book)
        if len(output) > 10:
            return f"{', '.join(output)[:10]}..."
        return f"{', '.join(output)}"

    def book_details(self, book):
        for line in self.books.readlines():
            single_line = line.split(', ')
            if single_line[0] == book.title():
                return f"{single_line[1]}, by {single_line[1]} costs {single_line[2]}."
        return "There is no such book.", self
