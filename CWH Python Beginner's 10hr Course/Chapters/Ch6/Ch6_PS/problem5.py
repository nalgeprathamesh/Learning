# Write a program to find whether a given user name is present in a list or not
name = ["Harry", "Larry" , "Marry" , "Barry" , "Tarry"]
username = input("Enter your name : ")

if(username in name):
    print("Your name is in the list")
else:
    print("Your name is not in the list")