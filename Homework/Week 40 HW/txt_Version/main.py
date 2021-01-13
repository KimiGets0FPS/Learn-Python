from books import Book
from users import Users
from manage import Manage


book = Book()
users = Users()
manage = Manage()


def menu():
    gusername = input("Enter your username: ")
    gpassword = input("Enter your password: ")
    if users.signin(gusername, gpassword) == True:
        while True:
            print("----------------------------------------")
            user_input = input(
                "1.) Borrow Books\n"
                "2.) Return Books\n"
                "3.) See Current Available books\n"
                "4.) See Current books you need to return\n"
                "5.) Book Details\n"
                "6.) Add Book (Require staff access)\n"
                "7.) Delete Book (Require staff access)\n"
                "8.) Modify Book (Require staff access)\n"
                "9.) Quit\n"
                "Your answer (enter the number): ")

            # Option 1, Borrow
            if user_input == '1':
                gbook = input("What book would you like to borrow: ")
                print(manage.borrow_book(gbook))

            # Option 2, Return
            elif user_input == '2':
                gbook = input("What book would you like to return: ")
                print(manage.return_book(gbook))

            # Option 3, See Current Available
            elif user_input == '3':
                print(book.current_available_books)

            # Option 4, See Current Return
            elif user_input == '4':
                print(book.current_return_books)

            # Option 5, Details
            elif user_input == '5':
                gbook = input("What book do you want to see: ")
                book.book_details(gbook)

            # Option 6, Add Book
            elif user_input == '6':
                getbook = input("Book title: ")
                getprice = input("Book price: ")
                getauthor = input("Book author: ")
                manage.add_book(getbook, getprice, getauthor)

            # Option 7, Delete Book
            elif user_input == '7':
                getbook = input("Book title: ")
                getconfimation = input("Are you sure (yes/no, default is yes): ")
                manage.delete_book(getbook, getconfimation)

            # Option 8 Modify Book
            elif user_input == '8':
                ...

            # Option 9, Quit
            elif user_input == '9':
                return "Thanks for coming!"

            else:
                print("There is no such option.")
    else:
        return 'Login failed.'


menu()
