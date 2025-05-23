# Write a program to calculate the factorial of a given number using loop
# 5! = 1*2*3*4*5
number = int(input("Enter the number: "))
multiplication = 1

for i in range(
    1, number + 1
):  # This help us make sure that numbers are multiplied from 1 to user entered number
    multiplication = multiplication * i  # This multiplies 1*2*3*...N

print(f"The factorial of {number} is {multiplication}")
