# protected access modifier only derived class  and within that class can access it
class Person:
    # constructor
    def __init__(self, name, age):
        self._name = name  # use single underscore for protected access modifier
        self._age = age


p1 = Person("kabir", 25)

# illegal way
print(p1._age)

# derived/inherited class


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print(f"name of the person is {self._name} and age is {self._age}")


s1 = Student("Rmia", 33)

s1.display_info()
