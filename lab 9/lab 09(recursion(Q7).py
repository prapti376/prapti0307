def avglist(l,n=None,s=0):
    if n is None:
        n=len(l)
    if n==0:
        if l:
            return s/len(l)
        else:
            return 0
    return avglist(l,n-1,s+l[n-1])
print(avglist([1,2,3]))        