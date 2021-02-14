#----------------- Object Decorator---------------------------------------------
def disply(name):
    print(name)

a=disply("DIPTI")
b=a
# Inner function----------------------------------------------------------------
def show():
    print("Dipti")
    def display():
        print("Bagal")
    display()
show()


#Syntatic decorator
def show(func):
    print("Dipti")
    def display():
        print("Shivaji")
        func()
    return display()
@show

def fun_new():
    print("Bagal")
fun_new()



