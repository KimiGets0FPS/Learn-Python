class Main:
    def __init__(self, names, books, lent_books=[], owe=0):
        self.names = names
        self.books = books
        self.lent_books = lent_books
        self.owe = owe

    def get_user(self, name, password):
        if name.title() in self.names:
            if int(password) == self.names.get(name.title()):
                return f'Hello {name.title()}!'
            return 'Wrong password'
        return 'Sorry, not a valid user'

    def get_book(self, getbook):
        if getbook.title() in self.books:
            return getbook.title()
        return 'Not a valid book'

    def delete_book(self, book, output=[]):
        if book.title() in self.books:
            del self.books[book.title()]
            for i in self.books:
                output.append(i)
            if len(output) > 10:
                output = output[:10]
            return f"Books that are available: {', '.join(output)}"
        return 'Not a valid book'
    
    def book_price(self, book):
        if book.title() in self.books:
            return self.books[book.title()]
        return 'Not a valid book'

    def lend_book(self):
        pass

    def return_book(self):
        pass

    def owe_money(self):
        pass


if __name__ == '__main__':
    main = Main({'Brian': 1234, 'Kimi': 5678, 'Ryan': 9012}, {'Harry Potter 1': 13, 'Harry Potter 2': 14, 'Harry Potter 3': 15}, [''])
    gname = input('Your name: ')
    gpassword = input('Your Password: ')
    print(main.get_user(gname, gpassword))
    dbook = input('Book that you want to delete: ')
    print(main.delete_book(dbook))
    gbook = input('Book that you want to get: ')
    print(main.get_book(gbook))
    pbook = input('Book you want to see how much it costs: ')
    print(main.book_price(pbook))
