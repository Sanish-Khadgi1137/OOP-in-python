# super class/parent class
class A:
    def feature1(self):
        print('feature 1A working')

    def feature2(self):
        print("Feature 2A workkking")

# single layer inheritance
# sub class/child class of A; B(A)


class B(A):
    def feature3(self):
        print('feature 3B working')

    def feature4(self):
        print("Feature 4B working!")

# Multi layer inheritance; not class C can used feature of both A and B


class C(B):
    def feature5(self):
        print('feature 5C working')

    def feature6(self):
        print("Feature 6C working!")

# a seperate class


class D:
    def featureD7(self):
        print('feature D7 working')

    def featureD8(self):
        print("Feature D8 working!")

# Multiple inheritance; which have all the feature of A and D too
#if E(C,D) e1 can access all the feature of class ABCD and E as C is the child of both A and B
class E(A, D):
    def feature9E(self):
        print('Feature 9E wotking!')


# a1 = A()  # creating object
# a1.feature1()
# a1.feature2()

# b1 = B()
# b1.feature3()
# # since B is chlid class so object of B i.e. b1 can access featuree 1 and 2 too
# b1.feature1()

# c1 = C()
# c1.feature1()
# c1.feature3()
# c1.feature5()

e1 = E()
e1.feature9E()
e1.feature1()
e1.featureD8()

