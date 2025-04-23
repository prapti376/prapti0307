g1={'bread':40,'butter':85,'nutella':300}
g2={'bread':2,'butter':3,'nutella':1}
total=0
for i in g1:
    for j in g2:
        if i==j:
            total+=(g1[i]*g2[i])
print('total bill:',total,'rs')