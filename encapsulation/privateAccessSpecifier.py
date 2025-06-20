#encapsulation allow us to control the access and visibility of variable and methods i.e Access Modifierhttps://www.youtube.com/watch?v=tyA4vD5BF3A

#private / have access within the class only
class Person:
    #constructor
    def __init__(self, name, age):
        self.__name = name #use double underscore for private access modifier
        self.__age = age

    def display_info(self):
        print(f"name of the person is {self.__name} and age is {self.__age}")

p1 = Person("kabir", 25)

#print(p1.__name)#can access private variable from outside

#illegal way; only available in py
#dir(p1) #we can see all variable and methods in collab format; and use it like below
print(p1._Person__name)


#llegal way /best way
p1.display_info()#method inside a same class; private data can be access only with by method inside same class