borrowed_books = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/borrowed.txt", "r")
books = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/books.txt", "r")


class Book:
    def specific_book_available(self, book):
        ...

    @property
    def current_available_books(self):
        available_books = []
        for book in books.readlines():
            bname = book.split(', ')
            if bname not in borrowed_books:
                available_books.append(bname)
        if available_books == []:
            return "There aren't any availlable books."
        if len(available_books) > 10:
            return f"{', '.join(available_books)[:10]}"
        return f"{', '.join(available_books)}"
    
    @property
    def current_return_books(self):
        ...

    def book_details(self, book):
        for line in books.readlines():
            sline = line.split(', ')
            if sline[0] == book.title():
                return f"{sline[1]}, by {sline[1]} costs {sline[2]}."
        return "There is no such book."
