# Create a class programmer for storing of programmers at microsoft

class programmer:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        print(f"{name} age is {age} and earns {salary}")
prathamesh = programmer("Prathamesh" , 17, 250000000)
harry = programmer("Harry" , 39, 20000000)
tarry = programmer("Tarry", 23 , 12000000)