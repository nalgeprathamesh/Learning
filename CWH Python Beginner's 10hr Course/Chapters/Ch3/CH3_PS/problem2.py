# Make a program that shows the user name and says that he is selected and user entered date at end

name = input("Enter your Name: ")
date = input("Enter Today's Date: ")
letter = f'''Dear {name},
You are selected!
{date}'''
print(letter)