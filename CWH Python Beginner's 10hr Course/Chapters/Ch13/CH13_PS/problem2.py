# Write a program to input name,marks and phone number and format it using format fun
# The name of student is {name} , their marks are {marks} and their phone number is {phone number}
name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone_number = input("Enter Phone Number: ")

a = "The name of student is {} , their marks are {} and their phone number is {}".format(name, marks, phone_number)
print(a)