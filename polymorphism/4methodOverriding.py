

# 2method overriding( 2 method with same name and a same parameters)
# eg: in inheritance both super and sub class have a method with same name and same(number of) parameters
class A:
    def show(self):
        print("in A show")


class b(A):
    #pass
    def show(self):
        print("in B show")
    
    
s = b()
s.show()