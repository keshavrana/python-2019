1. print statement

x=4
y=5
z=x+y
print(z)
x=x+2
print(x)
x+=2
print(x)
x-=3
print(x)

2. input from user

a=input("enter 1st value => ")
b=input("enter 2nd value => ")
c=int(a)+int(b)
print(c)

3. if condition

if True:
   print("keshav rana")

4. program of "if" condition
x=input("Enter a number => ")
r=int(x)%2
if r==0:
    print("your number is even")
else:
    print("your number is odd")

5. "Else" check whether number is positive or negative
x=int(input('enter a number '))
if x>0:
    print("number is positve ")
elif x==0:
    print("number is zero" )
else:
    print("number is negative")

6. "Elif" condition
x=4
if x==1:
    print("one")
elif (x==2):
    print("two")
elif (x==3):
    print("three")
elif (x==4):
    print("four")
else:
    print("wrong number")