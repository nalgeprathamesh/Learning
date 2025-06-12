# Write a program using enumerate to print 3rd,5th and 7th element from a list

l = [1,2,3,4,5,6,7,8,9,323,3,23,23,23]

for index, item in enumerate(l):
    if index==2 or index ==4 or index == 6:
        print(item)