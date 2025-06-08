# Repeat program 4 for list of 4 word which should be censored

words = ["world" , "donkey" , "prestigious" , "their"]

with open("CH9_PS//para.txt", "r") as f:
    content = f.read()

# content1 = content.lower()

# newContent1 = content1.replace(words[0], "#####")
# newContent2 = newContent1.replace(words[1], "#####")
# newContent3 = newContent2.replace(words[2], "#####")
# newContent4 = newContent3.replace(words[3], "#####")

# with open("CH9_PS//para.txt", "w") as f:
#     f.write(newContent4)

# Another smarter and shorter way
newContent = content.lower()  #Converts the text into lowercase
for word in words:
    newContent = newContent.replace(word, "#"*len(word))   #updating the same variable and updating newContent and also using # for the number of letters there are in a word

with open("CH9_PS//para.txt", "w") as f:
    f.write(newContent)     #overwrite newContent