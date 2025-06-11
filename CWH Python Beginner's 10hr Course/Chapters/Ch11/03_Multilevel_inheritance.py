class employee:
    a = 23

class programmer(employee):
    b = 43

class coder(programmer):
    c = 34

o = employee()  #This can only access it's own attributes
print(o.a)

p = programmer()   #This can access its own attribute alongside with employee()
print(p.a, p.b)

q = coder()
print(q.a, q.b , q.c)
# This allows use to inherit attributes of both employee() and programmer() in coder()