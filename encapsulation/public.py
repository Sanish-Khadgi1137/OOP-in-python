#Public can be accessed from any where
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name  # use no underscore for public access modifier
        self.age = age


p1 = Person("kabir", 25)

# llegal way
print(p1.name,p1.age)