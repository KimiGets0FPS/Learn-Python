class Calculator:
    """We don't need the __innit__ function for this problem"""
    def add(self, input_1, input_2):
        sum = input_1+input_2
        return sum

    def subtract(self, input_1, input_2):
        difference = input_1-input_2
        return difference

    def multiply(self, input_1, input_2):
        product = input_1*input_2
        return product

    def divide(self, input_1, input_2):
        quotient = input_1/input_2
        return quotient


calculator = Calculator()

print(f"\nThe sum is {calculator.add(4, 2)}")
print(f"The difference is {calculator.subtract(45, 5)}")
print(f"The product is {calculator.multiply(50, 2)}")
print(f"The quotient is {calculator.divide(50, 5)}")
