def international_greetings(name):
    guest_list = {"Randy": "Germany", "Karla": "France", "Wendy": "Japan", "Norman": "England", "Sam": "Argentina"}
    if name in guest_list:
        country = guest_list.get(name)
        return f"Hi! I'm {name}, and I'm from {country}"
    else:
        return f"Hi! I'm a guest"


print(international_greetings("Randy"))
