# Write a program to open 1.txt, 2.txt and 3.txt
# if any of these files are not present an message should be showcased 
# without exiting the program

try:
    with(
        open('1.txt') as f1,
        open('2.txt') as f2,
        open('3.txt') as f3
    ):
        print("Opened All files")
except Exception as e:
    print(e)

print("This program has not crashed!")