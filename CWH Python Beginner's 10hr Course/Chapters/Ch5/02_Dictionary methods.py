marks = {
    "Prathamesh":100,
    "Harry":90,
    "Larry":80
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Prathamesh":99 , "Lucy":10})
print(marks)
# Dictionary are mutable
print(marks.get("Tarry")) #Gives none
print(marks["Harry2"]) #Prints error