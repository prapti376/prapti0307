def create_list(l1,l2):
    s1=set(l1)
    s2=set(l2)
    return s1&s2
#main
l1=[1,2,3,3,4]
l2=[2,2,4,6]
print(create_list(l1,l2))