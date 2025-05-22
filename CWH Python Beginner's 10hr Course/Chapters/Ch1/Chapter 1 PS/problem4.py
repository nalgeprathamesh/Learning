import os

# Specifying the directory of the content
directory_path = '/'

# Lists all the files in directory or path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)