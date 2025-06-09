# Write a class train to which has methods to book a ticket,
# get status, get fare information of a train under Indian Railways

from random import randint #Helps us import specific things from specific modules

class train:
    def __init__(self,methods, status, fare):
        print(f'''This train can be booked by {methods} 
and the number of seats available are {status}
The fare is {fare}''')
        
train("Cash" , randint(0,100) , randint(344,7278))