# Write a program to find line number of 'python' from question 6


with open("CH9_PS//log.txt" , "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"It contains 'python' in line no {lineno}")
        break
    lineno += 1
else:
    print("It doesn't contain python")

# Logic used here is
# If a word doesn't contain 'python' then it checks another line by lineno+=1 and it continues to do
# so in the 'for loop' until it:
# Case A - find python , prints the line number and breaks
# Case B - doesnt find 'python' in 'for loop' and then checks else statements