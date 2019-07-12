#1. object class

class Dog():

    def __init__(self,breed,name,work):
        self.breed = breed
        self.name = name
        self.work = work

mydog=Dog(breed="desi",name="chiku",work="faltu")
print(mydog.breed)
print(mydog.name)
print(mydog.work)

#2. object class 2

class Circle():
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius

my=Circle()
print(my.radius)

#3. object function

class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return self.radius*self.radius*Circle.pi

my=Circle(4)
print(my.area())

#4. object function 2

class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return self.radius*self.radius*Circle.pi
    def set_radius(self,new_r):
        self.radius=new_r

my=Circle(3)
my.set_radius(999)
print(my.area())