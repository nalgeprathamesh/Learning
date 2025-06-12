# Exception handling is neccesary so that the program doesn't crash when an error arises
try:
    a = int(input("Enter a number: "))
    print(f"The number is {a}")
except ValueError as v:
    print("Please enter a valid number")
except Exception as e:
    print(e)  #This prints the error message if the error is different

print("Thank you, this program has not crashed")

# Error handling prevents an program from entirely crashing
# Lets say the user enter "jbnrwfgnrhn" instead of integer in this program
# Then it will just print the error but program will not crash
# It will print error: Please enter a valid number
# But after this program will still continue and it will print "Thank you, this program has not crashed"