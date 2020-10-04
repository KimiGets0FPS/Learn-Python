class Player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_name(self):
        return f"The player's name is {self.name.title()}"

    def get_age(self):
        return f"{self.name.title()} is {self.age}"

    def get_height(self):
        return f"{self.name.title()} is {self.height}"

    def get_weight(self):
        return f"{self.name.title()} is {self.weight}"


do = Player("john", 22, 180, 150)

print(do.get_name())
print(do.get_age())
print(do.get_height())
print(do.get_weight())
