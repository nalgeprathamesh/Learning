# Write a program to check whether a file is identical and matches the content of another file 
with open("CH9_PS//this.txt", "r") as f:
    content1 = f.read()

with open("CH9_PS//this1.txt", "r") as f:
    content2 = f.read()

if(content1==content2):
    print("The file is identical")
else:
    print("The file is not indentical")