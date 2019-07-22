#1.init function in python  

class Computer:
	def __init__(self,cpu,ram):
		self.cpu = cpu
		self.ram = ram

	def config(self):
		print("config is",self.cpu,self.ram)

com1 = Computer('keshav',6316035)
com2 = Computer('kamal',6316034)

com1.config()
com2.config()


#2.   Clsaa in python 

class Computer:
	def config(self):
		print("helllo world")
com1 = Computer()
Computer.config(com1)

#3. Student Average Marks 

class Student:
	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return(self.m1+self.m2+self.m3)/3

s1=Student(23,43,87)
print(s1.avg())

#4. Inheritance in python 

class student:
	def feature1(self):
		print("My ")

	def feature2(self):
		print("Name")


class college(student):
	def feature3(self):
		print(" Is ")

	def feature4(self):
		print("Keshav")


s1 = college()
s1.feature3()
print(college)

