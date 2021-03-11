from books import Book
from users import Users
from manage_books import Manage


book = Book()
users = Users()
manage = Manage()


def menu():
    get_username = input("Enter your username: ")
    get_password = input("Enter your password: ")
    if users.sign_in(get_username, get_password):
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
                print(manage.borrow_book(book=input("What book would you like to borrow: ")))

            # Option 2, Return
            elif user_input == '2':
                print(manage.return_book(book=input("What book would you like to return: ")))

            # Option 3, See Current Available
            elif user_input == '3':
                print(book.current_available_books)

            # Option 4, See Current Return
            elif user_input == '4':
                print(book.current_return_books)

            # Option 5, Details
            elif user_input == '5':
                book.book_details(input("What book do you want to see: "))

            # Option 6, Add Book
            elif user_input == '6':
                manage.add_book(book=input("Book title: "), price=input("Book price: "), author=input("Book author: "))

            # Option 7, Delete Book
            elif user_input == '7':
                get_book = input("Book title: ")
                get_confirmation = input("Are you sure (yes/no, default is yes): ")
                manage.delete_book(get_book, get_confirmation)

            # Option 8 Modify Book
            elif user_input == '8':
                ...

            # Option 9, Quit
            elif user_input == '9':
                print("Thanks for coming!")
                break

            else:
                print("There is no such option.")
    else:
        print('Login Failed')
    return


if __name__ == '__main__':
    menu()
