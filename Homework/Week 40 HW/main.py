from user_settings import User
from book import Book


# TODO: add modify book function
user = User({'Brian': [1234, 13], 'Ryan': [9012, 13]}, {'Kimi': [5678, 14]})
#! adding more details to books
booksetting = Book({'Harry Potter 1': ['J.K. Rowling', 13], 
    'Harry Potter 2': ['J.K. Rowling', 14], 
    'Harry Potter 3': ['J.K. Rowling', 20]}, 
    ['Harry Potter 1'], ['Harry Potter 2'],  ['Harry Potter 3'])


class Main:
    @property
    def library_main(self):
        get_name = input(f'You only get 1 chance...\nWhat is your username: ')
        get_passw = input(f'What is your password: ')
        if user.signin(get_name, get_passw) == True or 'Staff':
            while True:
                userinpt = input(""
                    "1.) Borrow Books\n"
                    "2.) Return Books\n"
                    "3.) See Current Avaliable books\n"
                    "4.) Book Details\n"
                    "5.) See How Much You Owe\n"
                    "6.) Book price\n"
                    "7.) Add Book (Require staff access)\n"
                    "8.) Delete Book (Require staff access)\n"
                    "9.) Modify Book (Require staff access)\n"
                    "10.) Quit\n"
                    "Your answer (enter the number): ")
                #! 1
                if userinpt == '1':
                    gbook = input('What book do you want to borrow: ')
                    print(booksetting.lend_book(gbook))
                #! 2
                elif userinpt == '2':
                    rbook = input('What book do you want to return: ')
                    print(booksetting.return_book(rbook))
                #! 3
                elif userinpt == '3':
                    print(booksetting.available_books)
                #! 4
                elif userinpt == '4':
                    cbook = input("What book details do you want to see: ")
                    print(booksetting.check_book(cbook))
                #! 5
                elif userinpt == '5':
                    print(user.owe_money(get_name.title()))
                #! 6
                elif userinpt == '6':
                    bprice = input("Enter the book that you want to see "
                    "how much it costs: ")
                    print(booksetting.book_price(bprice))
                #! 7, 8, and 9
                elif userinpt == '7' or userinpt == '8' or userinpt == '9':
                    # all requires admin access so it's better to make it together
                    if user.signin(get_name, get_passw) != 'Staff':
                        get_staff = input(f'What is your username: ')
                        get_pass = input(f'What is your password: ')
                        if user.signin(get_staff, get_pass) != 'Staff':
                            print('You are not a staff.')
                    else:
                        bbook = input('Book name: ')

                        if userinpt == '7':
                            bprice = input('Book price: ')
                            print(booksetting.add_book(bbook, bprice))
                        elif userinpt == '8':
                            print(booksetting.delete_book(bbook))
                        else:
                            """choice = input(""
                            "1.) Change Price ONLY\n"
                            "2.) Change Author ONLY\n"
                            "3.) Change both\n"
                            "Your Answer (enter number)")
                            gbook = input("Enter the book name you want to change: ")
                            if choice == '1':
                                gprice = input("Enter the new price for the book:")
                            elif choice == '2':
                                gauthor = input("Enter the new author for the book: ")
                            elif choice == '3':"""
                            gprice = input("Enter the book name you want to change: ")
                            guathor = input("Enter the new author for the book: ")
                            print(booksetting.modify(bbook, gprice, guathor))
                #! 10
                elif userinpt == '10':
                    break
                else:
                    print("That isn't a valid option.")
            return "Thanks for coming!"
        return "The username/password that you entered is invalid."


if __name__ == '__main__':
    main = Main()
    print(main.library_main)
