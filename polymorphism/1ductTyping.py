# dynamic typing
# here 'x' is just a name to a memory/space in mem
x = 5
print(type(x))

x = "nabin"
print(type(x))

#####################################################################################
# duck typing; if there is a bird and that bird behaves like duck, walks like a duck, quacks like a duck, it swims like a duck then it should be a duck


class Pycharm:
    def execute(self):
        print("compiling")
        print("running")

class Myeditor:
    def execute(self):
        print("compiling")
        print("running")
        print("spell check")
        print("convention check")



class Laptop:
    def code(self, ide):
        ide.execute()


lap1 = Laptop()

# #but missing a argument ide; but first we need to create object of ide
# lap1.code()

# #ide of type Pycharm()
# ide = Pycharm()
# #we can access the functions of the class whose object(here ide) is passed to another object(here lap1)
# #we can change the type of 'ide'(make object from other class); but that object/class must have required method(here execute()); we are not concern about which calss's object is it
ide = Myeditor()

lap1.code(ide)
