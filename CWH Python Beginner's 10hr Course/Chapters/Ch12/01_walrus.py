# Using Walrus Operators
# It is used to assign value and compare value simultaneously

if(n := len([1,2,3,4,5]))>3:
    print(f"List is too long({n} elements, expected < 3)")
    # Output - List is too long(5 elements, expected < 3)
else:
    print("List is shorter than 3 elements")