
# pattern in Python
i=10
while i>0:
    print('*'*i)
    i=i-1


# If Control example-1---------------------------------

Year=int(input("Enter the number "));
if Year%4==0 :
    print("Is leap year")


year=int(input("Enter the number "));

if year==2020 :
    print(2020)
elif year==2021:
    print(2021)

#------Example-2----------------------------------

marks=int(input("enter marks "))
if marks >=80 :
    print("Distintion")
elif marks >=70 and marks<80:
    print("First class")
elif marks>=60 and marks<70:
    print("Second class")
else:
    print("Fail")


#-----------Example-2---------------------------------------------------
a=10
b=20
c=30
if a>b and a>c:
    print(" gretest number is a=",int(a))
elif b>a and b>c :
    print("gretest number is b=",int(b))
else:
    print("gretest number is c=",int(c))



# For control------------------------------------

sum=0
for i in range(1,11) :
     sum=sum+i
print(sum)

# Fibonacci series-------------------------------------------------------

num1=0
num2=1
sum=0
print(num1)
print(num2)
for i in range(2,11):
    sum=num1+num2
    print(sum)
    num1=num2
    num2=sum


# While control---------------------------------------------------------------
'''
i=1
while i<=10 :
    print(i)
    i=i+1
    '''

# Do While-------------------------------------------------------------------- table of 2

i=1
while True:
    print(2*i)
    i+=1
    if i>10 :
        break
        

# Sum of digit

sum=0
num=int(input("enter the number "))
while num>0:
    rem=num%10
    sum=sum+rem

    num=num//10
print(sum)

# palindrome number--------------------------------------------------------------------
sum=0
num=int(input("enter the number "))
original=num
while num>0:
    rem=num%10
    sum=sum*10+rem

    num=num//10
#print(sum)
if(sum==original) :
    print("Number is Palindrome")
else :
    print("Number is not Palindrome")







