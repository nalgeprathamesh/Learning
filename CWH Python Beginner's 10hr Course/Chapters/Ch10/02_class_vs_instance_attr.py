class employee:
    age = 17
    salary = 10000000  # Class Attribute


prathamesh = employee()
prathamesh.salary = 12000000  # This is an instance attribute
print(employee.age, employee.salary)
# Instance attribute is given more priority than class attribute
