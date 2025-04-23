import random
l=[]
for i in range(20):
    l.append(random.randrange(0,100))
print(l)
x=int(input('enter a number: '))
for i in l:
    if i==x:
        