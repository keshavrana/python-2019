1. while loop

i=1
while i<=5:
    print("keshav ")
    i=i+1


2. Nested while loop

i=1
while i <= 5:
    print("keshav ", end="")
    j=1
    while j<=5:
        print("rana     ", end="")
        j=j+1
    i=i+1
    print()


3. for loop

l=['keshav',32,45,43,43242]
for i in l:
    print(i)


4. for loop itself define

for i in [23,233,'keshav']:
    print(i)


5. Break in python

av=10
a=int(input("How Many Candy You Want=>"))
i=1
while i<=a:
    if i>av:
        print("out of stock")
         braek

    print("Candy")
    i=i+1

6. Continue statement in python

for i in range(1,101):
    if i%5==0:
        continue
    print(i)


7. Pass statement in python

for i in range(1,101):
    if(i%2!=0):
        pass
    else:
        print(i)

