file = open("users.txt", "r")


class Users:
    def sign_in(self, username, password):
        for line in file.readlines():
            temp = line.split(', ')
            if temp[0] == username.title():
                if username.title() == temp[0] and password == temp[1]:
                    return True
            return False

    def is_staff(self, username, password):
        if username not in file.readlines():
            return "There is no such user."
        for line in file.readlines():
            line = line.split(', ')
            if username == line[0] and password == line[1]:
                if line[3]:
                    return True, self
                break
        return False, self
