# Write a program to copy a text file 'this.txt'

with open("CH9_PS//this.txt" , "r") as f:
    content = f.read()

with open(f"CH9_PS//this2.txt" , "w") as f:
    f.write(content)