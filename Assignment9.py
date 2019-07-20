#1. WAP a program to find Fctorial of a number

def fact(n):
	f=1

	for i in range(1,n+1):
		f=f*i

	return f

n=5
result=fact(n)
print(result)

#2. WAP a program to find Factorial using Recursion ''

def fact(n):
	if n==0:
		return 1

	return n*fact(n-1)	

result=fact(6)
print(result)


#3. WAP to find square a number 

def square(n):
	c=n*n
	print(c)
square(4)


#4. WAP to find square of a number using lambda

f=lambda a : a*a

result=square(5)
print(result)

