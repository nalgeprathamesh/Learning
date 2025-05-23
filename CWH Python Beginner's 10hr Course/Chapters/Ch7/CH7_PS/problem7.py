# Write a program to print the following star pattern for n = 3
#  *
# ***
# *****

# High complexity
n = int(input("Enter Number: "))
for i in range(1, n + 1):
    print(
        " " * (n - i), end=""
    )  # Number of spaces should be n-i, for first line(i=1) in n=3 there 2 spaces and 1 star
    print(
        "*" * (2 * i - 1), end=""
    )  # 2i-1 is used to create odd number of stars so for first line(i=1) there is 1 star , for i=2 there are 3 stars
    print("")

    # Print statements by default gives a new line so we add end = "" that does not create new line
