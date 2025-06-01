# Write a function to remove number from a list and strip it at same time

l1 = [0,1,2,3,4,5,6,7,8,9,10,24,424]

def r1(n):
    l1.remove(n)
    print(f"The following list is {l1}")


x = int(input("Enter the number you want to be removed: "))
r1(x) #This removes number at n'th index

# Alt way
# def rem(l1,num):
#     for item in l1:
#         l1.remove(num)
#         return l1
# print(rem(l1,2))