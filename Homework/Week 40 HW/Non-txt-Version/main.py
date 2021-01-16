from user_settings import User
from book import Book


user = User({'Brian': ['1234'], 'Ryan': ['2354']}, {'Kimi': ['3456']})

booksetting = Book({'Harry Potter 1': ['J.K. Rowling', '13'],
                    'Harry Potter 2': ['J.K. Rowling', '14']},
                    ['Harry Potter 1'], ['Harry Potter 2'])


def library_main():
    get_name = input('What is your username: ')
    get_passw = input('What is your password: ')
    if user.signin(get_name, get_passw) == True or 'Staff':
        print(f"Hello, {get_name.title()}!")
        while True:
            print('------------------------------------------')
            userinpt = input(
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

            #! 1
            if userinpt == '1':
                gbook = input('What book do you want to borrow: ')
                print(booksetting.borrow_book(gbook))

            #! 2
            elif userinpt == '2':
                rbook = input('What book do you want to return: ')
                print(booksetting.return_book(rbook))

            #! 3
            elif userinpt == '3':
                print(booksetting.see_available_books)

            #! 4
            elif userinpt == '4':
                print(booksetting.borrowed_book)

            #! 5
            elif userinpt == '5':
                cbook = input("What book details do you want to see: ")
                print(booksetting.check_book(cbook))

            #! 6, 7, and 8
            elif userinpt == '6' or userinpt == '7' or userinpt == '8':
                #* all requires admin access so it's better to make it together
                if user.signin(get_name, get_passw) != 'Staff':
                    get_staff = input(f'What is your username: ')
                    get_pass = input(f'What is your password: ')
                    if user.signin(get_staff, get_pass) != 'Staff':
                        print('You are not a staff.')
                else:
                    bbook = input('Book name: ')

                    #! 6
                    if userinpt == '6':
                        bprice = input('Book price: ')
                        bauthor = input('Book author: ')
                        print(booksetting.add_book(bbook, bprice, bauthor))

                    #! 7
                    elif userinpt == '7':
                        print(booksetting.delete_book(bbook))

                    #! 8
                    else:
                        gprice = input('Enter the new price for the book: ')
                        guathor = input('Enter the new author for the book: ')
                        print(booksetting.modify(bbook, gprice, guathor))

            #! 9
            elif userinpt == '9':
                break

            else:
                print("That isn't a valid option.")
        return "Thanks for coming!"
    return "The username/password that you entered is invalid."


if __name__ == '__main__':
    print(library_main())
