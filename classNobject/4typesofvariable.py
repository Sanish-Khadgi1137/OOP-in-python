#class/static variaable vs instance variable
class Car:
    wheels  = 4 #call variable; common for all the object(car)

    def __init__(self, milage, company):
        self.mil = milage  #instance variable, as object(car) changes these value also changes
        self.com = company #instance variable


c1=Car(8,"audi")
c2=Car(11, "Toyota")

#namespace is an area where you create and store object/variable; 1. class namespace 2. object/instance namespace

# making change in class namesapce
Car.wheels = 5
#this changes effect on all the objects

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)