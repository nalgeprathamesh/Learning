# Write a program to find the sum of first n natural numbers using while loop
number = int(input("Enter the number: "))
i = 0
sum = 0
# a = int((number/2)(number+1)) This doesnt work

while (
    i <= number
):  # This will help to ensure that the sum is only till the entered value
    sum += i  # This is continously adding the value of i starting from 1+2+3+.....n
    i += 1

print(sum)
