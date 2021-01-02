borrowed_books = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/borrowed.txt", "r")
books = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/books.txt", "r")


class Book:
    def specific_book_available(self, book):
        ...

    def current_available_books(self):
        ...

    def book_details(self, book):
        for line in books.readlines():
            sline = line.split(', ')
            if sline[0] == book.title():
                return f"{sline[1]}, by {sline[1]} costs {sline[2]}."
        return "There is no such book."
