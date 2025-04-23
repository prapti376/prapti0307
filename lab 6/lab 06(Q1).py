l=[('darshit','ashit','devang'),'ragi','ashna','darshini',('darshil',)]
boys=[]
girls=[]
for x in l:
    if isinstance(x,tuple):
        boys.extend(x)
    else:
        girls.append(x)

print('number of boys:',len(boys))
print('number of girls:',len(girls))