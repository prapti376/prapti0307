def convert(s):
     l=s.split()
     set1=set(l)
     l1=list(set1)
     l2=sorted(l1)
     s1=" "
     for i in l2:
          s1+=(i+' ')
     return s1
print(convert('prapti is good'))