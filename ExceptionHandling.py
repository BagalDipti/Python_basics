 #ZeroDivisionError

try :
    a=int(input("Enter number a "))
    b=int(input("Enter number b "))
    c=a/b
    print(c)
except:
    print("Error")
print("Code Executed Successfully...")    
    


#NameError
a = int(input("Enter number a "))
prit(a)       #------------Error-----------------------------------


#IOError


import os
open("","")



#EOFError

a=int(input())

def divide(x,y):
    try:
        c=x/y
        print(c)
    except ZeroDivisionError as e:
        print(e)



print(divide(10,2))
print(divide(10,0))


try:
    a=10
    b=0
    c=a/b
    raise ZeroDivisionError("Error")
except ZeroDivisionError as e:
    print(e)
finally:
    print("Code executed Successfully")


