class Book:
    def __init__(self, books, available_books=[], lend_books=[]):
        #* books: the books in a library
        self.books = books
        #* books that are available
        self.available_books = available_books
        #* lend_books: the books that the user lended
        self.lend_books = lend_books

    #* See the specific details about a specific book
    def check_book(self, book):
        if book.title() in self.books:
            book_info = self.books[book.title()]
            if book.title() not in self.lend_books:
                return f"{book.title()} (costing {book_info[1]}), by {book_info[0]}, is avaliable."
            return f"{book.title()} (costing {book_info[1]}), by {book_info[0]}, is not avaliable."
        return f"We don't have {book.title()} in this library."

    #! REQUIRES STAFF ACCESS
    def add_book(self, book, book_price, book_author):
        if book.title() in self.books:
            return f'The book {book.title()} is already in the library.'
        self.available_books.append(book.title())
        self.books[book.title()] = book_price
        self.books[book.title()] = book_author
        return 'Book added.'

    #! REQUIRES STAFF ACCESS
    def delete_book(self, book, output=[]):
        if book.title() in self.books:
            del self.books[book.title()]
            if book.title() in self.available_books:
                self.available_books.remove(book.title())
            elif book.title() in self.lend_books:
                self.lend_books.remove(book.title())
            for i in self.books:
                output.append(i)
            return 'Book deleted'
        return 'Not a valid book'

    def borrow_book(self, book):
        if book.title() in self.available_books:
            self.lend_books.append(book.title())
            self.available_books.remove(book.title())
            return 'Book is available and you borrowed it'
        return 'The book is not avialable'

    def return_book(self, book):
        if book.title() in self.lend_books:
            self.lend_books.remove(book.title())
            self.available_books.append(book.title())
            return 'Book returned'
        return f"{book.title()} isn't in your lend books list."

    #* The Current Avaliable Books
    @property
    def see_available_books(self):
        if bool(self.available_books) == False:
            return "There aren't any books available."
        if len(self.available_books) > 10:
            return f"Current available books: {', '.join(self.available_books[:10])}..."
        return f"Current available books: {', '.join(self.available_books)}"

    @property
    def borrowed_book(self):
        if bool(self.lend_books) == False:
            return "You don't need to return any books."
        if len(self.lend_books) > 10:
            return f"{', '.join(self.lend_books[:10])}..."
        return ', '.join(self.lend_books)

    # TODO: COMPLETE MODIFY BOOK FUNCTION
    def modify(self, book, new_price='', new_author=''):
        if book.title() in self.books:
            if new_price:
                self.books[book.title()][1] = new_price
            if new_author:
                self.books[book.title()][0] = new_author
            return f"{book.title()} has been succesfully modified."
        return "Not a valid book"
