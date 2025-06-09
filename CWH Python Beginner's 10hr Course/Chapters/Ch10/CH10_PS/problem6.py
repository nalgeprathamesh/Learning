# Can you change self paramter inside a class to something else

class employee:
    age = 17
    salary = 10000000 

    def getInfo(sf):
        print(f"The age is {sf.age} and salary is {sf.salary}")

prathamesh = employee()
prathamesh.salary = 12000000  # This is an instance attribute

employee.getInfo(prathamesh)

# Yes we can change self paramter inside a class to anything else we want and we can see that code run even if we have written 'sf' instead of 'self'