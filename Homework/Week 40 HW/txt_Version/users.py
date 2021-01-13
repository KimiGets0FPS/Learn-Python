file = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/users.txt", "r")


class Users:
    def signin(self, username, password):
        for line in file.readlines():
            line = line.split(', ')
            if username == line[0] and password == line[1]:
                return True
        return False

    def ifstsaff(self, username, password):
        if username not in file.readlines():
            return "There is no such user."
        for line in file.readlines():
            line = line.split(', ')
            if username == line[0] and password == line[1]:
                if line[3]:
                    return True
                break
        return False
