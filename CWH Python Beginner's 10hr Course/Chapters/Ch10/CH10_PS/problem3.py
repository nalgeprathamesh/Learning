# Create a class with class attribute a, create an object from it and set
# a directly using object.a = o . Does this change class attribute

class operator:
    a = 21  #class attribute

o = operator()
print(o.a) #Prints the class attribute because instance attribute is not present - 21
o.a = 0
print(o.a) #Prints the instance attribute because it is present - 0
print(operator.a)   #Prints the class attribute - 21

# No this does not change the fundamental class attribute because only instance attribute can be defined