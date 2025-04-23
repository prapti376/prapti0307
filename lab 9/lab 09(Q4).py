def sum_avg():
    e=float(input('enter english marks: '))
    m=float(input('enter math marks: '))
    s=float(input('enter science marks: '))
    ss=float(input('enter socal science marks: '))
    h=float(input('enter hindi marks: '))

    total=e+m+s+ss+h
    avg=total/5
    return total,avg
print(sum_avg())