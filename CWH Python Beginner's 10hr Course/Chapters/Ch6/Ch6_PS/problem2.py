# Write a program to find out whether a student have passed or failed if
# it requires atleast 33% marks in each subjects to pass Assume 3 subjects
# and take their input from user

subject1 = int(input("Enter marks of Subject 1: "))
subject2 = int(input("Enter marks of Subject 2: "))
subject3 = int(input("Enter marks of Subject 3: "))

avg = ((subject1+subject2+subject3)/3)

if(avg > 40 and subject1>33 and subject2>33 and subject3>33):
    print("You have passed this exam with excellent percentage of", avg)
else:
    print("You have failed the exam with total percentage of", avg)