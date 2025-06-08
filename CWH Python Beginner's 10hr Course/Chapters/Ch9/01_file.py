# FILE I/0
f = open("file.txt" , "r") #Opens the file to read
data = f.read() #Reads the file contents
print(data)
f.close()