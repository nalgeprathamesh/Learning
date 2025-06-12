l = [3443,45,5,4]

# index = 0
# for item in l:
#     print(f"The number at index {index} is {item}")
#     index +=1

# This can be easily simplified using enumerate
for index, item in enumerate(l):
    print(f"The number at index {index} is {item}")
