#1. Constructor in python 

class Student:  
	count = 0  
	def __init__(self):  
		Student.count = Student.count + 1  
s1=Student()  
s2=Student()  
s3=Student()
s4=Student()  
s5=Student()
print("The number of students:",Student.count)


#2. Method Overloading 
class A:
	def show(self):
		print("In A Show")

class B(A):
	def show(self):
		print("In B Show ")
	
a1 = B()
a1.show()



#3. Exception Handling


a=5
b=0
try:
	print(a/b)
sexcept Exceptoion:
	print("pagal zero ki sath multiply nhi hoti")

print("bye")




