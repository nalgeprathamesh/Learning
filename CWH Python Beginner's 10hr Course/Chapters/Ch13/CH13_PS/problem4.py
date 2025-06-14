# Write a program to filter a list of number which are divisblee by 5
def div(n):
    if n%5==0:
        return True
    return False

l = [1,2,3,4,5,6,7,8,9,10,11]

a = filter(div, l)
print(list(a))