class employee:
    company = "Microsoft"
    def info(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"The name of employee is {self.name} and salary is {self.salary}")

# We can inherit all the properties of class employee using inheritance

class programmer(employee):   #This inherits all the properties of class employee #Also this is an single inheritance
    company = "Microsoft Windows"
    def status(self):
        print(f"The employee {self.name} is currently inactive")

a = employee()
b = programmer()

print(a.info("Prathamesh", 1200000), b.company)