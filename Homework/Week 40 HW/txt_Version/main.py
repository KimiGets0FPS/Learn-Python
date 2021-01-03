from books import Book
from users import Users
from manage import Manage


book = Book()
users = Users()
manage = Manage()


def menu():
    gusername = input("Enter your username: ")
    gpassword = input("Enter your password: ")
    if users.signin(gusername, gpassword) == 'True' or users.signin(gusername, gpassword) == 'Staff':
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

            #! Option 1
            if user_input == '1':
                gbook = input("What book would you like to borrow: ")
                print(manage.borrow_book(gbook))

            #! Option 2
            elif user_input == '2':
                gbook = input("What book would you like to return: ")
                print(manage.return_book(gbook))

            #! Option 3
            elif user_input == '3':
                print(book.current_available_books)

            #! Option 4
            elif user_input == '4':
                print(book.current_return_books)

            #! Option 5
            elif user_input == '5':
                gbook = input("What book do you want to see: ")
                book.book_details(gbook)

            #! Option 6
            elif user_input == '6':
                ...

            #! Option 7
            elif user_input == '7':
                ...

            #! Option 8
            elif user_input == '8':
                ...

            #! Option 9
            elif user_input == '9':
                ...

            else:
                print("There is no such option.")
    else:
        return 'Login failed.'


menu()
