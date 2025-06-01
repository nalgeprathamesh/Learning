# We use def to make a new function
# Functions are standa rd custom format to define a custom step

def avg():  #This is the definition of function
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    c = int(input("Enter Number 3: "))
    average = (a+b+c)/3
    print("The integer average of following number is :" , int(average))

#        
def greet():
    name = input("Enter your name: ")
    print("Good day", name)


greet() #We need to call functions to start them
avg()