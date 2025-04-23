s=str(input('enter a string: '))
ac=0
dc=0
for i in s:
    if i.isalpha():
        ac+=1
    elif i.isdigit():
        dc+=1
print('number of alphabets: ',ac)
print('number of digits: ',dc)