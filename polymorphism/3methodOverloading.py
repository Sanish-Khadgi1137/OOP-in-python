# #1method overloading(in a class have 2 method with same name but different parameters) in java, C++ but not in python
# eg: for py we can do it by little logical changes
class Student:

    # def sum(self,a,b):
    #     s = a + b
    #     return s

    # def sum(a,b,c):#we can't do this in python
    #     s = a+b+c
    #     return s
#############################################################################################
    # def sum(self, a=None, b=None, c=None):  # but we can do this instead of above 2 methods; setting parameters to by default None; if values is given None replace by that value else will excute as None

    #     s = 0

    #     if a != None and b != None and c != None:
    #         s = a + b + c

    #     elif a != None and b != None:
    #         s = a + b

    #     elif a != None:
    #         s = a

    #     return s
######3333333333333333333333333333333333333333333333333333333333333333333333333333333
    # OR using *args
    def sum2(self, *args):
        s = 0

        for num in args:
            s += num

        return s


s1 = Student()

#
# print(s1.sum())

print(s1.sum2())
# in python we can't create 2 method with same name in a class