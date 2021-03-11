class Manage:
    def __init__(self):
        self.read_borrowed = open("C:/Users/zhewe/OneDrive/Documents/Coding Projects/Learn-Python/Homework/Week 40 "
                                  "HW/txt_Version/borrowed.txt", "r")
        self.read_books = open("C:/Users/zhewe/OneDrive/Documents/Coding Projects/Learn-Python/Homework/Week 40 "
                               "HW/txt_Version/books.txt",
                               "r")
        self.edit_ = open("C:/Users/zhewe/OneDrive/Documents/Coding Projects/Learn-Python/Homework/Week 40 "
                          "HW/txt_Version/borrowed.txt", "w")
        self.edit_books = open("C:/Users/zhewe/OneDrive/Documents/Coding Projects/Learn-Python/Homework/Week 40 "
                               "HW/txt_Version/books.txt", "w")

    def borrow_book(self, book):
        for line in self.read_borrowed.readlines():
            if book.title() == line:
                return 'Book borrowed'
        return 'There is no such book'

    def return_book(self, book):
        for line in self.read_borrowed.readlines():
            if book.title() == line:
                return 'Book can be returned'
            return 'There is no such book'

    def add_book(self, book, price, author):
        if book and price and author:
            for i in self.edit_books.readlines():
                print(i)
            return "Book added."
        return "Need full information!"

    def delete_book(self, book, confirm='Yes'):
        if book.title() in book:
            if confirm.title() == 'Yes':
                if book.title() in self.read_borrowed:
                    ...
            return "Delete book cancelled."
        return "There is no such book."

    def modify_book(self, book, title='', price=0, author=''):
        if book in self.read_borrowed:
            if title.title():
                ...
            if price:
                ...
            if author.title():
                ...
            return "Book successfully modified."
        return "There is no such book."
