# Write a program from given file poems.txt and find out whether it contains word 'twinkle'

with open("CH9_PS/poems.txt") as f:
    data = f.read()  # read the whole file as a single string
    if "twinkle" in data.lower():  # also make it case-insensitive if needed
        print("This file contains 'twinkle'")
    else:
        print("It doesn't contain 'twinkle'")
