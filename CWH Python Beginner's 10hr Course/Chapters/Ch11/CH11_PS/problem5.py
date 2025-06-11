# Write a class vector representing a vector of n dimensions . Overload the + and * operator which calculates the sum and dot product of them

class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        result = vector(self.x + other.x, self.y + other.y , self.z + other.z)
        return result
    def __mul__(self,other):
        result = vector(self.x * other.x, self.y * other.y , self.z * other.z)
        return result
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

print("Write i,j and k for 1st number")  
i1 = int(input("Enter i: "))
i2 = int(input("Enter j: "))
i3 = int(input("Enter k: "))

a = vector(i1,i2,i3)

print("Write i,j and k for 2md number")  
i4 = int(input("Enter i: "))
i5 = int(input("Enter j: "))
i6 = int(input("Enter k: "))

b = vector(i4,i5,i6)

print(f"The addition of 2 following vectors is {a+b}")
print(f"The multiplication of 2 following vectors is {a*b}")