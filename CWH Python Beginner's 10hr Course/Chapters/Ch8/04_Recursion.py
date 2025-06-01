'''
    We know that 5! = 5*4*3*2*1
    n! = n * (n-1) * (n-2) * (n-3)...... 3*2*1
    n! = n * (n-1)!
    Basically,
    Factorial(n) = n * Factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n = int(input("Enter the number: "))
print(f"The factorial of the following number is: {factorial(n)}")

# We need to be careful while using recursion so that the functions doesn't keep get called infinitely