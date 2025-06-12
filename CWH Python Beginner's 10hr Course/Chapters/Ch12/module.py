def name():
    print("I am class from module.py")

name()
print(__name__)  #This will give output as '__main__' here but in 09_main.py it will give output as 'Module'

if name == "__main__":
    # If this code is run by it's own file
    print("We are directly running this code")
else:
    print("We are not directly running this code")