class employee:
    age = 17
    salary = 10000000  # Class Attribute

    def __init__(self, name, age, salary):  # dunder method which is automatially called
        self.salary = salary  #We have made an positional argument of 'salary'
        self.age = age
        self.name = name
        print("I am creating an object")

    @staticmethod  # Addition of this verifies that the below function is independent of class and doesn't need any arguments
    def greet():
        print("Good Morning")


prathamesh = employee("Prathamesh", 18, 1300000)  #We have substitued the positional arguments in the class employee
prathamesh.salary = 12000000  # This is an instance attribute

print(prathamesh.name, prathamesh.age, prathamesh.salary)
