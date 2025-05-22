# Last letter starts from -1 and moves -2,-3 and so on
name = "Prathamesh"
print(name[-10:-1])
# This is basically same as
print(name[0:9])

print(name[:4]) #It is same as print(name[0:4])
print(name[1:]) #It is same as print(name[1:10])
print(name[3:]) #It is same as print(name[3:10])

# Slicing with Skip values
word = "amazing"
print(word[1:7:2]) #Gives mzn value
# It basically does this operation
# First print(word[1:7]) which gives 'mazing'
# Then it skips 2 letters each starting from m then z and then n
