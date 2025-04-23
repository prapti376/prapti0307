l=[(1,2,),(2,3,4),(),(5,6,),()]
for i in l:
    if i == ():
        l.remove(i)
print(l)
#Remove empty tuple(s) from the list of tuples.


