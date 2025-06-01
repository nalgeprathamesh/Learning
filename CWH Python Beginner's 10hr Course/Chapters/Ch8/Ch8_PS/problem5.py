# Write a recursive function to print
# ***
# **
# *

a = int(input("Enter the number: "))

def pattern(n):
    if n==0:
        return
    print("*"*n)
    pattern(n-1)

pattern(a)
