# A file contains the word donkey multiple times you need to replace it with ##### and update the file

word = "donkey"

with open("CH9_PS//donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word , "#####")
            
with open("CH9_PS//donkey.txt", "w") as f:
    f.write(contentNew)


