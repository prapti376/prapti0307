def sanitizelist(l,i=0):
    if i>=len(l):
        return l
    elif l[i]<0:
        l[i]=0
    return sanitizelist(l,i+1)
print(sanitizelist([-1,2,3,-4]))