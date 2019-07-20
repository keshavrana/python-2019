#1. Numpy matrix

from numpy import *
m1=matrix('1 2 3 ; 2 3 4 ; 6 5 3')
m2=matrix('1 2 3 ; 3 4 6 ; 6 5 4')
m3=m1 + m2
print(m3)

#2. Function in python

def keshav():
    print("Hello")
    print("Welcome Back")
keshav()

#3. Add Function in python 

def add(x,y):
    c=x*y
    return c


result = add(2,3)
print(result)

#4. Add, Check Condition Function in python 

def add(a,b):
	c=a+b
	print(c)
	if c==0:
		print("Number Is Greater")

	else:
		print("Number Is Less Than ")	

add(4,6)


#5. String Function 

def person(name,age):

	print('Name => '+name)
	print(age)
person('keshav',34)	 



#6. Keyword Argument

def person(**data):


	for i,j in data.items():
		print(i,j)

person(name='keshav',age='23',city='mumbai',Number='9756748283')



