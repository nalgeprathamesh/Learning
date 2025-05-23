# Write a program to print the following star pattern for n = 3
# *
# **
# ***

# Medium complexity
n = int(input("Enter Number: "))
for i in range(1, n + 1):
    print("*" * (i), end="")
    print("")
