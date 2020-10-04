class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.first_name = last_name

    def full_name(self):
        first_name = self.fname.title()
        last_name = self.lname.title()
        fullname = f"{first_name} {last_name}"
        return fullname

    def email(self):
        first_name = self.fname.lower()
        last_name = self.lname.lower()
        email = f"{first_name}.{last_name}@gmail.com"
        return email


do = Person("john", "smith")

print(do.full_name())
print(do.email())
