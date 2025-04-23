def frequency(s):
    l=s.split()
    l2=sorted(l)
    for i in l2:
        print(len(i))
frequency('cat on mat')