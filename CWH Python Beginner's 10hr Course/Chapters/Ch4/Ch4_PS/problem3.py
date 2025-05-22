# Check that a tuple type cannot be changed by python
# Tuple cannot be changed
a = (23,24,True, "Prathamesh")
a[2] = False
print(a)

# This gives an error bcz tuple values cant be changed
# Error - 'tuple' object does not support item assignment