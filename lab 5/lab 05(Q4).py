import random
l=[]
n=[]
p=[]
for i in range(30):
    l.append(random.randrange(-30,30))
for i in l:
    if i<0:
        n.append(i)
    elif i>=0:
        p.append(i)
print(l,n,p,sep='\n')