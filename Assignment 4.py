# 1. condition statement

a=1
while a<5:
    print("welcome aliens")
    a=a+1

print("welcome ethical hacker")


#2. check condition

a=input("enter your email id")
print("welcome -"+a)
x=int(input("enter your paasword=> "))
print(x)

if x == 8449406995:
    print("wlcome hacker")
else:
    print("Try agin")

#3. check odd and even

a=int(input("enter any number "))
b=a%2
if b==0:
    print('the number is odd')
if b==1:
    print("the number is even")


#4.matrix pattern

for i in range(4):
    for j in range(i+1):
        print("#",end=" ");

print()

#5. list and condition check

nums=[43,13,43]
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")


#6. prime number

num=9
for i in range(2,num):
    if num%i==0:
        print("NOT PRIME")
        break
else:
    print("prime")

#7. print list
from array import *
val=array('i',[9,5,-2,4,3])
for i in range(0,5):
    print(i)

num=[6,5,3,6,7]
for i in num:
    print(i)
x=input("enter your name ")
y=int(input("enter your lucky number "))
if y==1234:
    print("welcome keshav")
else:
    print("please try again")