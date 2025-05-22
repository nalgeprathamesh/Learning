# Write a program to calculate grade of the students from their marks
marks = int(input("Enter your total Percentage: "))

if(marks > 90 and marks < 100):
    print("Your Grade is : Ex")
elif(marks > 80 and marks < 90):
    print("Your Grade is : A")
elif(marks > 70 and marks < 80):
    print("Your Grade is : B")
elif(marks > 60 and marks < 70):
    print("Your Grade is : C")
elif(marks > 50 and marks < 60):
    print("Your Grade is : D")
else:
    print("Your Grade is : F")
    print("Please contact your teacher if you believe this is a mistake or if you want to retake the exam")