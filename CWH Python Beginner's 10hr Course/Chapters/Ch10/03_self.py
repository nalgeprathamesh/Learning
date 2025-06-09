class employee:
    age = 17
    salary = 10000000  # Class Attribute

    def getInfo(self):
        print(f"The age is {self.age} and salary is {self.salary}")

    @staticmethod  # Addition of this verifies that the below function is independent of class and doesn't need any arguments
    def greet():
        print("Good Morning")


prathamesh = employee()
prathamesh.salary = 12000000  # This is an instance attribute

# The given below code are same things written in different manner
# prathamesh.getInfo()
employee.greet()
employee.getInfo(prathamesh)
