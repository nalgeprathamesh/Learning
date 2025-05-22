# Ask 4 users their name and their favourite language and showcase it in a dictionary
a = input("Enter your name: ")
e = input("Enter your favourite language: ")
b = input("Enter your name: ")
f = input("Enter your favourite language: ")
c = input("Enter your name: ")
g = input("Enter your favourite language: ")
d = input("Enter your name: ")
h = input("Enter your favourite language: ")
 
lang = {
    a:e,
    b:f,
    c:g,
    d:h
}
print(lang)

# Alternate way is to make a empty dictionary and use dict.update({name:lang})
# Note : key in dictionary can be only 1 but there can be multiple values
# Dict = {key:values}