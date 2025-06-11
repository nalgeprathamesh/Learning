# Create a class 2D Vector and use it to create another class 3d Vector
class vector_2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # print(f"The x coordinate is {x} and y coordinate is {y}")

class vector_3d(vector_2d):
    def Properties(self, x, y,z):
        super().__init__(x,y)
        self.z = z
        print(f"The x,y and z coordinates are {x}, {y} and {z} respectively")

a = vector_3d(23,43)
a.Properties(12,12,12)

b = vector_2d(43,93)
print(b.x, b.y)