# Create a program to find number of zeros in a following tuple
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
d = int(input("Enter Number 4: "))
e = int(input("Enter Number 5: "))
num = (a,b, c,d,e)
# print(num[0]+num[1]+num[2]+num[3]+num[4]) for fun
zeros = num.count(0)
print(zeros)