# # __init__ is a special(has __X__) method; which call automatically function or variable inside it
# class Computer:

#     def __init__(self):
#         print("in init!!!")

#     def configR(self):
#         print("i5, 8gb, 1tb")


# com1 = Computer() #constuctor call the __init__ automatically
# com2 = Computer()

# com1.configR()

##################333333333333333333333333333333333333333333333333333333333333333333

#passing argument to the class form object construction
class Computer:

    def __init__(self, cpu, ram, mem): #passed 4 argument 1. self is object(which is passed automatically whle construction) and other 3 cpu, ram and mem; 
        print("in init!!!")
        
        #assigninh passed argument to object
        self.cpu=cpu
        self.ram1=ram #can have different name too
        self.mem=mem



    def configR(self):
        print("Configuration of the computer are:", self.cpu, self.ram1, self.mem) #cpu,ram,mem are not locat varialbe, they belongs to object; to show refer to the object by self.cpu etc


com1 = Computer("i7","12gb","512gb")
com2 = Computer("ryzen 3","16gb","224bg")

com1.configR()

#binding variable and methond

