from user_settings import User
from book import Book


class Main:
    pass


if __name__ == '__main__':
    main = User({'Brian': 1234, 'Kimi': 5678, 'Ryan': 9012}, 13)
    #! input name and check password
    gname = input('Your name: ')
    gpassword = input('Your Password: ')
    print(main.signin(gname, gpassword))
    #! owe money
    omoney = input('Do you want to see if you owe any money (yes/no): ')
    print(main.owe_money(omoney))
#*----------------------------------------------------------------------------------------------------------------------------------------*#
    booksetting = Book({'Harry Potter 1': 13, 'Harry Potter 2': 14, 'Harry Potter 3': 15},  ['Harry Potter 3'])
    print(booksetting.available_books)
    #! a book you want to get
    gbook = input('Book that you want to get: ')
    print(booksetting.get_book(gbook))
    #! deleting a book
    dbook = input('Book that you want to delete: ')
    print(booksetting.delete_book(dbook))
    #! how much the book is worth
    pbook = input('Book you want to see how much it costs: ')
    print(booksetting.book_price(pbook))
    #! borrowing a book
    bbook = input('What book do you want to borrow: ')
    print(booksetting.lend_book(bbook))
    #! returning a book
    rbook = input('What book do you want to return: ')
    print(booksetting.return_book(rbook))
    #! looking at avialable books
    # abook = input('Do you want to see what are the current available books (Yes/No): ')
