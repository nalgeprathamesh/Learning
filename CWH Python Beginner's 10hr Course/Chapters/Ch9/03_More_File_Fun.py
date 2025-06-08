f = open("file.txt")
# lines = f.readlines() #Reads all the lines

# lines = f.readline() #Reads 1st line
# lines = f.readline() #Reads 2nd line
# print(lines, type(lines))
# f.close()

line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()