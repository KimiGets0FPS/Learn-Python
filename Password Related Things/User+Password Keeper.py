import json

filename = "username and password keeper.json"


def get_stored_password():
    try:
        with open(filename) as f:
            password = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return password


def get_stored_username():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_stored_name():
    try:
        with open(filename) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name


def get_new_name():
    name = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(name, f)
    return name

def get_new_username():
    username = input("What is your username? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def get_new_password():
    password = input("What is your password? ")
    with open(filename, 'w') as f:
        json.dump(password, f)
    return password
    


def greet_user():
    name = get_stored_name()
    username = get_stored_username()
    password = get_stored_password()
    if name and username and password:
        print(f"Welcome back, {name.title()}!")
        print(f"Username:{username}\nPassword:{password}")
    else:
        username = get_new_username()
        password = get_new_password
        name = get_new_name()
        user_last_chance = input(f"Username:{username}\nPassword:{password}\nAre these information correct?(y/n) ")
        user_last_chance = user_last_chance.lower()
        if user_last_chance == 'yes':
            print(f"We'll remember you when you come back {name.title()}!")
        else:
            pass


greet_user() 