# #if only  the super class has __init__/constructor
#  class A:

#     #constructor
#     def __init__(self):
#         print('I am class A')


# class B(A):
#   pass

# # inheritance if sub class has no constructor/__init__; it call the constructor of superclass
# c1=B()

# 333333333333333333333333333333333333333333333333333333

# #if both super and sub class have their own constructor/__init__
# class A:

#     #constructor
#     def __init__(self):
#         print('I am class A')


# class B(A):
#     def __init__(self):
#         print("init B ")

# #both had init; by default, it call construtor of own __init__
# c1=B()


# 333333333333333333333333333333333333333333333333333333333333333333333

# #if we want sub class to call constructor/init from both classes
# class A:

#     #constructor
#     def __init__(self):
#         print('init A')


# class B(A):


#     def __init__(self):
#         super().__init__()
#         print("init B ")

# #call both he constructor
# c1=B()


# 333333333333333333333333333333333333333333333333333333333333333333333333

#Method Resolution Order MRO; in case of multiple inheritance it will start inherit from left to right
class A:
    def __init__(self):
        print('init A')

    def feat(self):
        print('feature A')

    def feature2(self):
        print(" Feature A2")


class B:
    def __init__(self):
        print("init B ")

    def feat():
        print('Feature B')


class C(A, B):
    def __init__(self): #@1
        super().__init__() #@2
        print("init C")

#use of super method to call other functions too not only constructor
    def feature(self):
        super().feature2()

#it call init of A then C no B
#@1 goes to init of own, @2 find super().__init__() go to A due to MRO, @1 return found own init then print it
c1 = C()

#similar to about init/constructor, due to mro if both A and B have function of same name; sub class takes feat of most left
c1.feat()

c1.feature()
