def listoftuples(n):
    l=[]
    t=()
    for i in range(1,n+1):
        t=(i,i**2,i**3)
        l.append(t)
    return(l)
print(listoftuples(3))
