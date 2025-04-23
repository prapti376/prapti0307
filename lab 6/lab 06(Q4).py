l=[('bread',80),('butter',50),('cheese',100)]
for i in range(2):
    for j in range(2):
        if l[i][1]<l[j][1]:
            l[i],l[j]=l[j],l[i]
print(l)       