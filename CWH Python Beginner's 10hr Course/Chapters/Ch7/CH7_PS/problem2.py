# Write a program to greet all persons name stored in list l starting with S
l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if name.startswith("S" or "s"):
        print(f"Welcome {name}")
