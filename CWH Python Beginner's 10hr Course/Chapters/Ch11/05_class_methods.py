class employee:
    a = 1
    @classmethod  #This doesn't allow to update class attribute
    def show(cls):
        print(f"The class attribute is {cls.a}")

e = employee()
e.a = 93  #This will update the instance attribute
e.show()    #This will still show class attribute as 1 because we have added @classmethod which prevents instance attribute