# import math


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


def main():
    while True:
        x = int(input("First number: "))
        op = str(input("Operation: "))
        y = int(input("Second number: "))
        cal = Calculator(x, y)
        if op == '+':
            print(f"Answer: {cal.add()}")
        elif op == '-':
            print(f"Answer: {cal.subtract()}")
        elif op == '*':
            print(f"Answer: {cal.multiply()}")
        elif op == '/':
            print(f"Answer: {cal.divide()}")
        else:
            print("Enter something else (+ - * /)")
        print("-" * 100)


if __name__ == '__main__':
    print(main())
