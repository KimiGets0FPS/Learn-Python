class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.list_name = last_name

    def full_name(self):
        first_name = self.first_name.title()
        last_name = self.list_name.title()
        fullname = f"{first_name} {last_name}"
        return fullname

    def email(self):
        first_name = self.first_name.lower()
        last_name = self.list_name.lower()
        email = f"{first_name}.{last_name}@gmail.com"
        return email


do = Person("john", "smith")

print(do.full_name())
print(do.email())
