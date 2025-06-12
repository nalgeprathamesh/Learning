def fun():
    global a
    a = 434

fun()
print(a)  #This will throw an error if a is not global variable