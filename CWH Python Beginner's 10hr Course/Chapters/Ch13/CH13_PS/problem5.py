# Write a number to find maximum of numbers using reduce
from functools import reduce
numbers = [75755,56667,6678,7565,343554]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,numbers))