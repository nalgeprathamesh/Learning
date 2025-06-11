class employee:
    a = 23
    def __init__(self):
        print("I am Employee")

class programmer(employee):
    b = 43
    def __init__(self):
        print("I am programmer")

class coder(programmer):
    c = 34
    def __init__(self):
        super().__init__()  #This helps calling the def __init__ from the father class(programmer)
        print("I am Coder")

o = employee()  #This can only access it's own attributes
print(o.a)

p = programmer()   #This can access its own attribute alongside with employee()
print(p.a, p.b)

q = coder()
print(q.a, q.b , q.c)
# This allows use to inherit attributes of both employee() and programmer() in coder()