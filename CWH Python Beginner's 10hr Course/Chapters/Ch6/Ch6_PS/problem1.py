# Write a program to find the greatest of 4 numbers entered by user
a = int(input("Write Number 1: "))
b = int(input("Write Number 2: "))
c = int(input("Write Number 3: "))
d = int(input("Write Number 4: "))
e = [a , b , c ,d]
e.sort()
print("The largest Number is:",e[3])

# Other way harry used here is to write 4 ifelse statements but it is highly inefficient so i used different method