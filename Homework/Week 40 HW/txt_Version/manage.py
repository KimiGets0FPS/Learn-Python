borrowed = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/borrowed.txt", "r")
books = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/books.txt", "r")

class Manage:
    def borrow_book(self, book):
        for line in borrowed.readlines():
            if book.title() == line:
                edit_file = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/borrowed.txt", "w")

                return 'Book borrowed'
        return 'There is no such book'

    def return_book(self, book):
        for line in borrowed.readlines():
            if book.title() == line:
                return 'Book can be returned'
            return 'There is no such book'

    def add_book(self, book, price, author):
        if book and price and author:
            ...
        return "Need full information!"

    def delete_book(self, book, confirm='Yes'):
        if confirm.title() == 'Yes':
            ...
        return 'Delete book cancelled.'

    def modify_book(self, book, title='', price=0, author=''):
        if book in borrowed:
            if title.title():
                ...
            if price:
                ...
            if author.title():
                ...
            return "Book successfully modified."
        return "There is no such book."
