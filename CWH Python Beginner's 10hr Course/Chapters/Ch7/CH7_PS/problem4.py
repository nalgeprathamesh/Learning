# Write a program to find whether a given number is prime or not
number = int(input("Enter the number: "))

for i in range(2, number):
    if (number % i) == 0:
        print("This number is not a prime number")
        break
else:
    print("This number is a prime number")

# We have used the remainder function becauce remainder of non prime number is always 0 when divided by its divisors
# But prime numbers always have a remainder number
