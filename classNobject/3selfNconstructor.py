# class Computer:
#     pass #pass is used in when there is no attribute and methond in the class, which enable empty class

# c1 = Computer()
# c2 = Computer()

# #object are save in heap mem in our pc
# #address of object in heap mem is
# print(id(c1))#id changes in each run
# print(id(c2))

# #size of the object is depent upon number of variable and size of each variable
# #constructor is responsible for assigning the mem/allocate the size of object

################33333333333333333333333333333333333333333333333333333333333333333333333333333333

# #default value of class and changing it; showing the importance of "self"
# class Computer:
#     def __init__(self):
#         self.name = "rabin" #defalut vaules
#         self.age = 55

#     def update(self):
#         self.age = 40 #self is needed to say which object is to change


# c1 = Computer()
# c2 = Computer()


# #before any changes i.e default values
# print(c1.name, c1.age)
# print(c2.name, c2.age)

# #if we want to change the default value
# c1.name = "Suhana"


# #changing default value by calling function
# c2.update() #object c2 call update functon

# print(c1.name, c1.age)
# print(c2.name, c2.age)


#############33333333333333333333333333333333333333333333333333333333333333333333333333333333333

#compare method; showing the importance of "self"
class Computer:
    def __init__(self):
        self.name = "rabin" #defalut vaules
        self.age = 55

    def update(self):
        self.age = 40 #self is needed to say which object is to change


    def compare(self, other): #here self is caller object and other is whom to compare with
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

print(c1.name, c1.age)
print(c2.name, c2.age)

if c1.compare(c2):
    print("They are same")
else:
    print("They are differnt")

c2.update() 

print(c1.name, c1.age)
print(c2.name, c2.age)

if c1.compare(c2):
    print("They are same")
else:
    print("They are differnt")
    



    
    