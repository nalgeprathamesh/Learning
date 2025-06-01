# Print the table of number n
def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

x = int(input("Enter the number: "))
multiply(x)