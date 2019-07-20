#1. List into function 
def count(lst):
	even=0
	odd=0


	for i in lst:
		if i%2==0:
			even+=1

		else:
			odd+=1
	return even,odd

lst=[20,22,13,14,15,16,17,18]	
even, odd = count(lst)
print(even)
print(odd)

#2. Fibonacci sequence in python 

def fib(n):
	a=0
	b=1

	print(a)
	print(b)

	for i in range(2,n):
		c=a+b
		a=b
		b=c
		print(c)

fib(10)

#3. Fibonacci sequence only 1 has to print


def fib(n):
	a=0
	b=1

	if n==1:
		print(a)
	else:
		print(a)
		print(b)

		for i in range(2,n):
			c=a+b
			a=b
			b=c
			print(c)

fib(1)

