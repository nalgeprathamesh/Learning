# Write a recursive function to calculate sum of first n natural numbers

'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(n) = 1+2+3+4+5+........n
sum(n) = sum(n-1) + n
'''

def sum(n):
    if(n == 1): #This prevents from n going negative and decreasing the value
        return 1
    return sum(n-1)+n

print(sum(4))





# Alternate way using function
# n = int(input("Enter the number: "))

# def natural():
#     print("The sum of numbers is:" , (n/2)*(n+1))

# natural()