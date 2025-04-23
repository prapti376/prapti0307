def count_alpha_digits(s):
    ca=0
    cd=0
    for i in s:
        if i.isalpha()==True:
            ca+=1
        elif i.isdigit()==True:
            cd+=1
    print({'alphabets':ca,'digits':cd})
count_alpha_digits('prapti123')