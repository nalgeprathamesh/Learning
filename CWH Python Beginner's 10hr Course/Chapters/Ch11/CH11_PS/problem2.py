# Create a class 'pets' from class 'animal' and further create a class 'dogs' from
# class 'pets'. Add a method 'bark' to class 'dogs'

class animal:
    pass

class pets(animal):
    pass

class dogs(pets):
    @staticmethod
    def bark():
        print("Bark")

a = dogs()
dogs.bark()

# We have used Multi level inheritance here
