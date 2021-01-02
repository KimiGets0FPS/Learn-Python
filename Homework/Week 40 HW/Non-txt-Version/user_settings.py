class User:
    def __init__(self, users, staff):
        #* users
        self.users = users
        #* staff
        self.staff = staff

    def signin(self, name, password):
        if name.title() in self.staff:
            spassword = self.staff[name.title()]
            if password == spassword[0]:
                return 'Staff'
        else:
            upassword = self.users[name.title()]
            if password == upassword[0]:
                return True
            return False

    def owe_money(self, name):
        if name.title() in self.staff:
            value_list = self.staff[name.title()]
        else:
            value_list = self.users[name.title()]
        if value_list[1] == None:
            return "You don't owe any money"
        return f"You owe {value_list[1]} dollars"
