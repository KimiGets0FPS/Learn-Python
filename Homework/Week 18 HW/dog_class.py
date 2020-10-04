class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog("Sir. Bites A lot", 3)  # A dog that bites anything that it can find for no reason
your_dog = Dog("Sir. Licks A lot", 6)  # A dog that licks anything that is can find also for no reason

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\n\nYour dog's name is {your_dog.name}")
print(f"Your dog's age is {your_dog.age}")
your_dog.sit()
