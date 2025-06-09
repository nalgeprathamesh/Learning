# Add a static method in problem 2 to greet user 'Hello'
# Write a class calculator capable of finding square,cube and square root of a number

class calculator:
    def __init__(self,square,cube,square_root):
        print(f"The square of number is {square**2}")
        print(f"The cube of number is {cube**3}")
        print(f"The square root of number is {square_root**0.5}")
    @staticmethod
    def greet():
        print("Hello")

calculator.greet()
a = int(input("Enter the number you want square of: ")) 
b = int(input("Enter the number you want cube of: "))
c = int(input("Enter the number you want square root of: "))
calculator(a,b,c)