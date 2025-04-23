#Delete an element of a tuple.

t1 = (1,2,3,4,5)
l1 = list(t1)

l1.remove(4)
t1=tuple(l1)
print(t1)