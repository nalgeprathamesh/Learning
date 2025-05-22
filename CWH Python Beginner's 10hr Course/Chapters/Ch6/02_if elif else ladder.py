age = int(input("Enter your age: "))

# Start of 1st if statements
if(age>18 and age<110):
    print("Congratulations , You are above the age of 18")
elif(age<0):
    print("Sorry , Aliens and time travellers not allowed")    
elif(age>=110):
    print("Sorry, Ghost and dead people not allowed")
elif(age==0):
    print("Sorry, Babies not born are not allowed")
else:
    print("Sorry, you dont fit into any of our criteria so you are not allowed")
# End of 1st if statements

# Start of 2nd if statements
if(age%2==0):
    print("Congrats , Your age is even!")
else:
    print("Congrats , Your age is odd")
# End of 2nd if statements
# Note - If you write an if statement after other if statements that a new if statement is created
# and both of them will be executed separtely