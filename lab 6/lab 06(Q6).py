#Modify an element of a tuple.

t1 = (1,2,3,4,5)
l1 = list(t1)

l1[0]= 11
t1=tuple(l1)
print(t1)