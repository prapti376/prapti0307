import random
l=[]
r=[]
for i in range(50):
    l.append(random.randint(1,30))
print(l)
for i in l:
    if i not in r:
        r.append(i)
print(r)