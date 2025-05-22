# Write a program to enter marks of 6 students and sort them
a = int(input("Enter marks of student 1: "))
b = int(input("Enter marks of student 2: "))
c = int(input("Enter marks of student 3: "))
d = int(input("Enter marks of student 4: "))
e = int(input("Enter marks of student 5: "))
f = int(input("Enter marks of student 6: "))
marks = [a,b,c,d,e,f]
marks.sort()
print(marks)

# Alternate way would be making a empty list and then using append
