# Sometimes we need to raise intentional error so that a program behaves as expected
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

if(b == 0):
    raise ZeroDivisionError("Division by zero is not fundamentally defined")
    # This will intentionally raise our custom error message when b=0 and program will crash
else:
    print(f"The value of a/b is {a/b}")


print("This program has not crashed!")