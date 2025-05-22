# Write a program to sum a list with four number
list = []

a = int(input("Enter Number 1: "))
list.append(a)
b = int(input("Enter Number 2: "))
list.append(b)
c = int(input("Enter Number 3: "))
list.append(c)
d = int(input("Enter Number 4: "))
list.append(d)

print(list[0]+list[1]+list[2]+list[3])
# Alternate and easier way is
print(sum(list))