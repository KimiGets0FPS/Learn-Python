class Manage:
    def borrow_book(self, book):
        if book.title() in self.availiable_books:
            self.lend_books.append(book.title())
            self.occupied_books.append(book.title())
            self.availiable_books.remove(book.title())
            return 'Book is available and you borrowed it'
        return 'The book is not avialable'

    def return_book(self, book):
        if book.title() in self.lend_books:
            self.lend_books.remove(book.title())
            self.occupied_books.remove(book.title())
            self.availiable_books.append(book.title())
        return f"{book.title()} isn't in your lend books list."

    #* The Current Avaliable Books
    @property
    def available_books(self):
        temp = []
        for i in self.availiable_books:
                temp.append(i)
        if len(self.books) > 10:
            return f"Current available books: {', '.join(temp[:10])}..."
        return f"Current available books: {', '.join(temp)}"

    # TODO: COMPLETE MODIFY BOOK FUNCTION
    def modify(self, book, new_price='', new_author=''):
        if book.title() in self.books:
            if new_price:
                self.books[book.title()][1] = new_price
            if new_author:
                self.books[book.title()][0] = new_author
            return f"{book.title()} has been succesfully modified."
        return "Not a valid book"