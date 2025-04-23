import random
odd=[]
even=[]
for i in range(5):
    odd.append(random.randrange(1,9,2))
for i in range(4):
    even.append(random.randrange(0,11,2))
odd[3]=even
print(odd)
l1=[]
for x in odd:
    l1.extend(x) if isinstance(x,list) else l1.append(x)
l1.sort()
print(l1)