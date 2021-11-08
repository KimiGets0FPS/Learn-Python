fin = open("passwords.txt", 'r')
fout = open("passwords.txt", 'a')


def find(place: str, user: str):
    while True:
        thing = fin.readline().split()
        if not thing:
            return "Can't Find Domain (Create a new profile)"  # Didn't find
        domain, user_pass = ''.join(thing).split(':')
        username = ''.join(user_pass.split()[0])
        if domain == place and user == username:
            return ''.join(user_pass.split()[1])
        elif domain == place and user != username:
            return 'Invalid Username'


def new(place: str, user: str, password: str):
    output = f"{place}:{user} {password}"
    print(output, file=fout)
    return "New Profile Added."


def edit(place: str, user='', password=''):
    ...


def main():
    print('Hit the enter key to exit')
    while True:
        print("\n---------------------------------------\n")
        print(f"1. Find Password\n2. Create New Profile\n3. Edit Profile\n")
        dec = input("Enter a number: ")
        if dec == '1':
            domain = input('Enter a domain: ')
            username = input('Enter a username: ')
            print(find(domain, username))
        elif dec == '2':
            domain = input('Enter a domain: ')
            username = input('Enter a username: ')
            password = input('Enter the password: ')
            print(new(domain, username, password))
        elif dec == '3':
            domain = input('Enter a domain: ')
            username = input('Enter a username: ')
            password = input('Enter the password: ')
            print(edit(domain, username, password))
        elif dec == '\n':
            print('Thanks for coming!')
            return
        else:
            print('Invalid operation')


if __name__ == '__main__':
    # print(fin.readline())
    main()
    exit()
