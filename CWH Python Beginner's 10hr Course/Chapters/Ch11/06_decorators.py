class employee:
    a = 1
    @classmethod  #This doesn't allow to update class attribute
    def show(cls):
        print(f"The class attribute is {cls.a}")
    @property  #We have defined a property here
    def name(self):
        return f"{self.fname} , {self.lname}"
    @name.setter   #We will take name and then split it behind the scene. This is called encapsulation
    def name(self,value):
        self.fname = value.split(" ")[0]    #This will divide the name into 2 parts where first empty space is found
        self.lname = value.split(" ")[1]


e = employee()
e.a = 93  
e.show()   
e.name = "Prathamesh Nalge"
print(f"The first word is {e.fname} and the second word is {e.lname}")

# We use split value function to break into 2 things in a list
# a = "Prathamesh Nalge"
# a.split(" ") #This means that divide the string wherever it sees single space
# a = ["Prathamesh", "Nalge"]