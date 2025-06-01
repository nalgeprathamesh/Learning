# Write a python program to convert celsius to farnheit
celsius = int(input("Enter the temperature(in C): "))


def temp(celsius):
    print(f"The following temperature in farnheit is: {round(1.8*celsius + 32 , 3)}")


temp(celsius)

# Here we have used the round function to round the value where round(number, number of digits)
