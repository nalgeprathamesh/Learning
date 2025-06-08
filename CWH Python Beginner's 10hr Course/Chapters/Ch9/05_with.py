f = open("file.txt")
print(f.read())
f.close()

# The same can be written more efficiently and with higher value with (with) statements
with open("file.txt") as f:
    print(f.read())

# There is no need to close file with (with) statements