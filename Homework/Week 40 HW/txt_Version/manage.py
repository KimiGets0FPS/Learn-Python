file = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/borrowed.txt", "r")


class Manage:
    def borrow_book(self, book):
        for line in file.readlines():
            if book.title() == line:
                edit_file = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/borrowed.txt", "w")
                
                return 'Book borrowed'
        return 'There is no such book'

    def return_book(self, book):
        for line in file.readlines():
            if book.title() == line:
                return 'Book can be returned'
            return 'There is no such book'
