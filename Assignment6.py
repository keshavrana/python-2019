#1. Inheritance in python
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def WhoAmI(self):
        print("animal")
    def eat(self):
        print("food")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

my=Dog()
my.WhoAmI()
my.eat()


#2. Special Method

class Book():

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return "Title: {}, Author: {},Pages: {}".format(self.title,self.author,self.pages)

b=Book("python","keshav","200")
print(b)


#3. Regular Expression
import re
patterns=['term1','term2']
input='This is a string with term2, but not the other!'
for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern,input):
        print("MATCH!")
    else:
        print("NOT MATCH!")


