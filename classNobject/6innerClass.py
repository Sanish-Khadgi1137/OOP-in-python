# outter class
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # creating the object of inner class(Laptop) inside the outter class
        #self.lap = self.Laptop

    def show(self):
        print(self.name, self.rollno)

    # inner classs/class inside class
    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Sudha", 5)
s2 = Student("Rudha", 6)

# print(s1.name, s1.rollno)
# instead of above print lets use function
s1.show()

# #becuase lap object is inside of student class
# s1.lap.brand

#or
# lap1 =s1.lap
# lap2 =s1.lap

# print(id(lap1))
# print(id(lap2))

# directly creating object of inner(laptop) ouside of the outter class
lap1 = Student.Laptop()
#show from Laptop
lap1.show()

print(lap1)
