# Write a program to print multiplication table of a number using for loop
number = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{number} X {i} = {i*number}")
