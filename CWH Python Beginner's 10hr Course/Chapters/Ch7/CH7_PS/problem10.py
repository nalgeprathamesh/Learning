# Make a program to print multiplication table of n using for loops in reverse order
number = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{number} X {11-i} = {(11-i)*number}")

    # Just did 11-i in place of i from 1st problem
