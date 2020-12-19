# import sys
# print(sys.executable)
class User:
    def __init__(self, names, owe=0):
        self.names = names
        self.owe = owe

    def signin(self, name, password):
        if name.title() and password:
            if name.title() in self.names:
                if int(password) == self.names.get(name.title()):
                    return f'Welcom {name.title()}!'
                return 'Wrong password'
            return 'Invalid user'

    def owe_money(self, desicion):
        if desicion.title() == 'No':
            return None
        if self.owe == 0:
            return "You don't owe any money!"
        return f'You owe {self.owe} dollars!'
