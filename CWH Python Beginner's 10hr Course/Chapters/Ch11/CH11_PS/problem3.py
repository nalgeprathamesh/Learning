# Create a class employee and add salary and increment properties to it
class Employee:
    salary = 78753
    increment = 20

    @property
    def Salary_after_increment(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @Salary_after_increment.setter
    def Salary_after_increment(self,salary):
        self.increment = ((salary/self.salary)-1)*100

a = Employee()
a.Salary_after_increment = 100000
print(a.increment)