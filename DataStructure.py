
#=============LIST===============================================================

List=['Hello',10,"Dipti",7]
print(List)
print(List[1:3])
print(List[-1])
print(List[-4: -3])

#============================LIST Operations==========================================

List1=[1,2,3,4,5]
List2=[6,7,8,9,10]
print(List1+List2)
print(List1*2)
print(List1[1:5])
print(List2[-4:-1])

List=[]
sum=0
n=int(input("Number of elements  "))
for i in range(0,n) :
    element=int(input())
    List.append(element)
    sum=sum+element
print(List)
print("Sum of elements is",sum)

#----------------------------Copy the elements---------------------------------------------------------
List1=[1,2,3]
List2=list(List1)
print(List2)


#-------------------------Tuple-----------------------------------------------------------------------

Tup=(1,'Dipti', 7,'Bagal,2')
print(Tup)
print(type(Tup))

List=[1,2,3,7]
tuple1=tuple(list)
print(tuple1)


tup=(1,2,3,4,5,6,7,8)
num=int(input("Enter the number which u want to search  "))
if num in tup:
    print("Present")

else:
    print("Not Present")


#==================Disctionary===============================================

My_dist={1:5, 2:"Dipti", 3:"Bagal", 4:90, 5:"Hi Dip", 6:[1,2,3]}
print(My_dist)

print(My_dist.keys())
print(My_dist.values())
print(My_dist.copy())

print("value is  "+My_dist[5])


def fun():
    x=10
    print(x)
x=x=1
fun()







