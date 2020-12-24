class Book:
    def __init__(self, books, availiable_books=[], lend_books=[], occupied_books=[]):
        # books: the books in a library
        self.books = books
        # books that are available
        self.availiable_books = availiable_books
        # lend_books: the books that the user lended
        self.lend_books = lend_books
        # occupied_books: the unavailable books that other users borrwoed.
        self.occupied_books = occupied_books

    @property
    def available_books(self):
        temp = []
        for i in self.availiable_books:
                temp.append(i)
        if len(self.books) > 10:
            return f"Current available books: {', '.join(temp[:10])}..."
        return f"Current available books: {', '.join(temp)}"

    #* See the specific details about a specific book
    def check_book(self, book):
        if book.title() in self.books:
            book_price = self.books[book.title()]
            if book.title() not in self.occupied_books:
                return f"{book.title()}, by {book_price[0]}, is avaliable."
            return f"{book.title()}, by {book_price[0]}, is not avaliable."
        return f"We don't have {book.title()} in this library."

    #! REQUIRES STAFF ACCESS
    def add_book(self, book, book_price):
        if book.title() in self.books:
            return f'The book {book.title()} is already in the library.'
        self.books[book.title()] = book_price
        return 'Book added.'

    #! REQUIRES STAFF ACCESS
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
            self.lend_books.append(book.title())
            self.availiable_books.remove(book.title())
            return 'Book is available and you borrowed it'
        return 'The book is not avialable'

    def return_book(self, book):
        if book.title() in self.lend_books:
            self.lend_books.remove([book.title()])
            self.availiable_books.append(book.title())
        return f"{book.title()} isn't in your lend books list."

    # TODO: COMPLETE MODIFY BOOK FUNCTION
    def modify(self, book, price='', author=''):
        if book.title() in self.books:
            if price:
                ...
            if author:
                ...
            return f"{book.title()} has been succesfully modified."
        return "Not a valid book"
