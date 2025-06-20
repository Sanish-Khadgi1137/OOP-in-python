#class is a blue print
class Computer:
    #self is the object we are passing
    def configR(self): #function inside a class is called 'method'
        print("i5, 8gb, 1tb")



#making instances/object of class computer; constructor
com1 = Computer()
com2 = Computer()


print(type(com1))

# #calling method of the class
# Computer.configR(com1) #here self = com1

# Computer.configR(com2)


#another way
#using object itself to call the function
com1.configR() #here behind the scene congicR(take com1 as argument and pass in 'self')



#https://www.youtube.com/watch?v=qiSCMNBIP2g