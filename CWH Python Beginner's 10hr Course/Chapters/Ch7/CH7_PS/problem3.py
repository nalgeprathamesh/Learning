# Write a program to print multiplication table of a number using while loop
number = int(input("Enter the number: "))

i = 1
while i < 11:
    print(f"{number} X {i} = {i*number}")
    i += 1
