

# ------------Single Inheritance-----------------------
class A:
    def Show(self):
        print("Parent class")

class B(A):
    def Disply(self):
        print("Child Class")

p=A()
c=B()
c.Show()
c.Disply()


# -----------Multiple Inheritance-------------------------------


class A:
    def Show(self):
        print("Parent class")
class B():
    def DisplyB(self):
        print(" B class")
class C(A,B):
    def DisplyC(self):
        print("C class")
b=B()
c=C()
b.Show()
b.DisplyB()
c.Show()
c.DisplyC()


# ------------------Multilevel Inheritance------------------
class A:
    def Show(self):
        print("Parent Class")

class B(A):
    def DisplayB(self):
        print("B class")
class C(B):
    def Displayc(self):
        print("C class")

a=A()
b=B()
c=C()
c.Show()
c.DisplayB()
c.Displayc()


#------------------Hierarchical Inheritance-------------------------------------------

class A:
    def Show(self):
        print("Parent Class")

class B(A):
    def DisplayB(self):
        print("Class B")
class C(A):
    def DisplayC(self):
        print(" Class C")

class D(A):
    def DisplayD(self):
        print("Class D")

b=B()
c=C()
d=D()
b.Show()
b.DisplayB()
c.Show()
c.DisplayC()
d.Show()
d.DisplayD()



#--------------Hybride Inheritance--------------------------------------
class D():
    def DisplyD(self):
        print("C class")

class B(D):
    def DisplayB(self):
        print("Class B")
class C(D):
    def DisplyC(self):
        print(" B class")

class A(B,C):
     def DisplayA(self):
         print(" Class A")
a=A()
b=B()
c=C()
d=D()
b.DisplayB()
b.DisplyD()
c.DisplyC()
c.DisplyD()
a.DisplyD()
a.DisplyC()
a.DisplayB()
d.DisplyD()
