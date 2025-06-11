# Write a program that generates a random number and ask the users to guess it
# If the user guusses lower number tell them it's a higher number
# If the user guusses higher number tell them it's a lower number

import random

random_number = random.randint(1, 10000)

print("Welcome to Perfect Guess. Just predict the correct number using hints")

i = 0
while True:
    user_number = int(input("Enter the number: "))
    if user_number > random_number:
        print("Enter lower Number.")
    elif user_number < random_number:
        print("Enter Higher Number.")
    else:
        print(f"You have gussed the correct number {random_number} in {i} attempts")
        break
    i += 1

# Question completely solved in 1st attempt