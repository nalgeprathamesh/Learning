dict1 = {"a": 3, "b": 4}
dict2 = {"b": 2, "c": 7}
merged = dict1 | dict2
print(merged)  # Output: {'a': 3, 'b': 2, 'c': 7}

# Also we can open multiple files at once

with open("file1.txt") as f1, open("file2.txt") as f2:
    a = f1.read()
    b = f1.read()
    if a==b:
        print("Both files are same")
    else:
        print("Both files are different")