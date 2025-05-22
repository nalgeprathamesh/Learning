import random
import pyttsx3

print("***Welcome to the Spy ID Generator***")
name = input("Enter your Real name: ")
code = input("Enter your Secret code name: ")
year = input("Enter your Joining year: ")
status = input("Enter your mission status(Success/Failure): ")

print("Generating ID")

print('''==============================
||    SECRET AGENT ID CARD   ||
==============================
''')

random.seed(10)

masked = code[:3]+"*****"
status = status.upper()
ID = code.upper() + "-" + year[-2:] + str(random.randint(1,10000))

print(f'''|| Name       : {name}
|| Code Name  : {masked}
|| Joined     : {year}
|| Status     : {status}
|| ID String  : {ID}
==============================
''')

engine = pyttsx3.init()
engine.say(f'''Welcome, Agent {masked}, Your status is {status}, Your ID is {ID}. 
           Congratulations on the status of the mission.
           Your old ID will now be disposed and new ID will be activated soon.
           Your payment since {year} will be automatically paid within 60 seconds
           Thank you for working with our secret organisation''')
engine.runAndWait()