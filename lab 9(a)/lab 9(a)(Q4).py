lst = ['madam','Python',"malayalam",12321]
def palindrome(s):
    l=str(s)
    if l==l[::-1]:
        return s
    else: 
        return None
m=list(filter(None,map(palindrome,lst)))
print(m)