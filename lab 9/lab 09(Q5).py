def ispangram(s):
    set1=set(s)
    set2=set()
    for i in range(97,123):
        set2.add(chr(i))
    print(set2.issubset(set1))
    
#main
ispangram("the quick brown fox jumps over the lazy dog")