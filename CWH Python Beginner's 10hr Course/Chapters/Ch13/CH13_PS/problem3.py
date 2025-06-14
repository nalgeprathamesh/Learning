# A list contains a multiplication table of 7. Convert it to vertical string of same numbers

l = [str(7*i) for i in range(1,11)]
b = "\n".join(l)
print(b)
