class Number:  # Class name should be capitalized
    def __init__(self, n):
        self.n = n

    # Dunder method for addition
    def __add__(self, num):
        return Number(self.n + num.n)  # Return a new Number instance

n = Number(1)  # Corrected class name
m = Number(2)
result = n + m
print(result.n)  # Access the 'n' attribute to print the value
