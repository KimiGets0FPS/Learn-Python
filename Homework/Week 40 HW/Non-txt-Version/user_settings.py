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
