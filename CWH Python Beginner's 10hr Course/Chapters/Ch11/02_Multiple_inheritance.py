class employee:
    company = "Microsoft"
    def info(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"The name of employee is {self.name} and salary is {self.salary}")

class personalInfo:
    def age(self, age):
        self.age = age
        print(f"The age is {self.age}")

class programmer(employee, personalInfo): #We have used multiple inheritance here and used properties from class employee and personalInfo
    company = "Microsoft Windows"
    def status(self):
        print(f"The employee {self.name} is currently inactive")

a = employee()
b = programmer()

b.age(12)
b.info("Prathamesh", 9899899)
b.status()
