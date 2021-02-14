

#-----------------Overriding in Python--------------------------------------------------------------------------------------------------------
class A:
    def show(self,a):
        print(a)

class B(A):
    def show(self,a):
        print(a)


a=A()
b=B()
a.show(10)
b.show(20)


#----------Python do not support Overloading----------------------------------------------------------------------------------------
class A:
    def show(self,a):
        print(a)

    def show(self,a,b):     #--------------------Error------------------------------------------
        c=a=b
        print(c)
a=A()
a.show(10)
a.show((10,20))