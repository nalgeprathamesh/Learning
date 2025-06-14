l = [1,2,3,4,5]

square = lambda x: x*x

# Map example
sqList = map(square,l)  #Map accepts map(function,iterable)
print(type(sqList))   #Output: Map Class
print(list(sqList))   #We need to convert it to list before printing result

# Filter example
def even(n):
    if(n%2 == 0):
        return True
    return False

evenList = filter(even, l)  #filter accepts filter(fun,iterable)
print(list(evenList)) #Output: [2, 4]

# reduce example
# we need to import reduce to use it
from functools import reduce

def sum(a,b):
    return a+b

print(reduce(sum,l)) #Output: 15. It has added everything in the list
# We have used sequential computation in this reduce method

mul = lambda x,y: x*y
print(reduce(mul,l))