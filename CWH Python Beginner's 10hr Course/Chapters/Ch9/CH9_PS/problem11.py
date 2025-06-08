# Write a python program to rename a file to renamed_by_python.txt
with open("CH9_PS//good.txt", "r") as f:
    content = f.read()

with open("CH9_PS//renamed_by_python.txt", "w") as f:
    f.write(content)

# We have basically just created a copy of good.txt and named it renam....
# We can just delete old file now and all we have left is renamed version
# To delete old file we can use OS Module