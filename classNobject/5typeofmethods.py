# 1.instance method(1.Accesor = which used to access , 2.Mutator = which used to modify), 2.Class method, 3.Static method
class Student:

    school = "KU"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # this is instance method as we are passing 'self'; to work with instance variable
    def avg(self):
        return ((self.m1+self.m2+self.m3)/3)
    
    # #Accesor Method
    # def get_m1(self):
    #     return self.m1

    # #Mutator Method
    # def set_m1(self, value):
    #     self.m1 = value

    #Class method(effect on all the objects) to work with class variable; always pass 'cls' and always used class decorator; with out decorator it ask for argument cls
    @classmethod
    def getSchool(cls):
        return cls.school
    
    #static method; not concern with both Class as well instance variable; eg. get sqaure etc
    @staticmethod
    def info():
        print('This is (static method)')


s1 = Student(34, 67, 32)
s2 = Student(89, 32, 32)

print(s2.avg())

print(Student.getSchool())

#this print out the static method
Student.info()
