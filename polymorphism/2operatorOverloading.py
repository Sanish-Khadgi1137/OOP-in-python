#we have different method for different operator
a = 4
b = 7

print(a + b)
#above print is actually runs like below; run with method '_add_' inside of the 'int' class; "ctrl+click on int" to see the "int class"
print(int.__add__(a,b))

p ="4"
q = "7"

print(p+q)
#same goes for string
print(str.__add__(p,q))

#but int + str wont work
print(a+q)

########################################################################################################3
#operator overloading(Define how operators behave for user-defined classes using methods like __add__, __eq__, etc.)

# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2


# s1=Student(58,69)
# s2=Student(60,65)

# #in general 2 objects and classes cannot be added, because our class does not have an add method
# s3 = s1 + s2

# print(s3)

#################################################################################################
# eg operator overloading/rewriting above code with 'add' functionality
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # function for '+' operator is __add__
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)  #new object s3 created; s3 is just naming we can name what ever we want

        return s3

    # method for ">" operator
    def __gt__(self, other):
        r1 = self.m1 + self.m2  # r1 is simple variable for integer
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

    # to print out; overloading(operator remains same operand(type of operand) changes) the print(__str__) method
    def __str__(self):
        # return  self.m1, self.m2#to address this error TypeError: __str__ returned non-string (type tuple)
        # on executing those curly brakets are replaced by values
        return '{} {}' .format(self.m1, self.m2)


s1 = Student(58, 69)
s2 = Student(80, 65)

stu3 = s1 + s2  #this is s3; actually happen Student.__add__(s1,s2)

print(stu3.m1)

# here s1 and s2 is simple variable for integer
if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

# if we want to perform operation in any user define object; we need to define that operation(method)

a = 3

print(a)  # give value in a # actuall code print(a.__str__())
print(a.__str__())

print(s1)  # give address # to make it to print values we need to override this method
print(s1.__str__())