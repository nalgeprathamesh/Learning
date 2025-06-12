# By predefining an variable as integer we can directly access all it's method

from typing import Tuple

n : int = 5

name : str = "Prathamesh"

def sum(a:int, b:int) -> int:
    return a+b

s = sum(5,5)   #It provides a hint what the positional arguments are. ie int and int
print(f"The sum is {s}")

person : tuple[int,str] = ("Prathamesh", 100) #We have used the typing module here to make to code more readble

print(person, type(person))