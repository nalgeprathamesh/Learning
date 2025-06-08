# Mine a log file and find out whether it contains 'python'

with open("CH9_PS//log.txt" , "r") as f:
    content = f.read()

content1 = content.lower()

if "python" in content1:
    print("It contains 'python' ")
else:
    print("It doesn't contain python")