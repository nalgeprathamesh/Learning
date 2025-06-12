# Write a program to display a/b where as os integer. Show infinity as error when user enter b==0

try:
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    c = a/b
    print(int(c))
except ZeroDivisionError as v:
    print("Infinity")
except Exception as e:
    print("Error")

print("Program not crashed")