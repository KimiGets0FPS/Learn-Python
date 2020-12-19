class Book:
    def __init__(self, books, lend_books=[], occupied_books=[]):
        self.books = books
        self.lend_books = lend_books
        self.occupied_books = occupied_books

    @property
    def available_books(self):
        temp = []
        for i in self.books:
                temp.append(i)
        if len(self.books) > 10:
            return f"Current available books: {', '.join(temp[:10])}..."
        return f"Current available books: {', '.join(temp)}"

    def get_book(self, getbook):
        if getbook.title() in self.books and getbook.title() not in self.occupied_books:
            return getbook.title()
        elif getbook.title() in self.occupied_books:
            return f"{getbook.title()} is being borrowed at the moment, please try again later."
        return 'Not a valid book'

    def delete_book(self, book, output=[]):
        if book.title() in self.books:
            del self.books[book.title()]
            for i in self.books:
                output.append(i)
            if len(output) > 10:
                output = output[:10]
            return f"Books that are available: {', '.join(output)}"
        return 'Not a valid book'
    
    def book_price(self, book):
        if book.title() in self.books:
            return f'The book {book.title()} costs {self.books[book.title()]} dollars'
        return 'Not a valid book'

    def lend_book(self, book):
        if book.title() not in self.occupied_books:
            self.occupied_books.append(book.title())
            return 'Book is available and you borrowed it'
        return 'The book is not avialable'

    def return_book(self, book):
        if book.title() in self.lend_books:
            self.lend_books.pop([book.title()])
        return f"{book.title()} isn't in your lend books list."


