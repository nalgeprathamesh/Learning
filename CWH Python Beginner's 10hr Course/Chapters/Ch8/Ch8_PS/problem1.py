# Write a program using functions to find the greatest of 3 user entered numbers

n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))

def greatest(n1,n2,n3):
    l1 = [n1,n2,n3]
    l1.sort()
    print(f"The greatest number is {l1[2]}")

greatest(n1,n2,n3)

# Alternate method would be to use if statements to compare numbers
# but it would be highly non efficient to write multiple if else statements