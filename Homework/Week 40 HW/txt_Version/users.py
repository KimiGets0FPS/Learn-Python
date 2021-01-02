file = open("C:/Users/zhewe/Coding Projects/Learn-Python/Homework/Week 40 HW/txt_version/users.txt", "r")


class Users:
    def signin(self, username, password):
        for line in file.readlines():
            line = line.split(', ')
            if username == line[0] and password == line[1]:
                if line[3]:
                    return 'Staff'
                return 'True'
        return 'False'
