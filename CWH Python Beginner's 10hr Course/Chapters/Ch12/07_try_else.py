try:
    a = int(input("Enter a number: "))
    print(f"The number is {a}")
except Exception as e:
    print(e)  #This prints the error message if the error is different
else:
    print("Thank you, this program has not crashed")

# The else statement only gets executed if try block is succesful
# else statement does not run if try block gives an error