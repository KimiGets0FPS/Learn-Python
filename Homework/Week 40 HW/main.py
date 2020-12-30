from user_settings import User
from book import Book


# TODO: add modify book function
user = User({'Brian': ['1234', '13'], 'Ryan': ['9012', '13']}, {'Kimi': ['5678', '14']})
#! adding more details to books
booksetting = Book({'Harry Potter 1': ['J.K. Rowling', '13'], 
    'Harry Potter 2': ['J.K. Rowling', '14']}, 
    ['Harry Potter 1'], ['Harry Potter 2'])


class Main:
    @property
    def library_main(self):
        get_name = input(f'You only get 1 chance...\nWhat is your username: ')
        get_passw = input(f'What is your password: ')
        if user.signin(get_name, get_passw) == True or 'Staff':
            while True:
                print('------------------------------------------')
                userinpt = input(""
                    "1.) Borrow Books\n"
                    "2.) Return Books\n"
                    "3.) See Current Available books\n"
                    "4.) See Current books you need to return\n"
                    "5.) Book Details\n"
                    "6.) See How Much You Owe\n"
                    "7.) Add Book (Require staff access)\n"
                    "8.) Delete Book (Require staff access)\n"
                    "9.) Modify Book (Require staff access)\n"
                    "10.) Quit\n"
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
                #! 6
                elif userinpt == '6':
                    print(user.owe_money(get_name.title()))
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
                            bauthor = input('Book author: ')
                            print(booksetting.add_book(bbook, bprice, bauthor))
                        elif userinpt == '8':
                            print(booksetting.delete_book(bbook))
                        else:
                            gprice = input('Enter the new price for the book: ')
                            guathor = input('Enter the new author for the book: ')
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
