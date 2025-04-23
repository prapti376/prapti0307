def grades(s):
    if 0<=s<=39:
        return 'Grade: F'
    if 40<=s<=44:
        return 'Grade: P'
    if 45<=s<=49:
        return 'Grade: C'
    if 50<=s<54:
        return 'Grade: B'
    if 55<=s<=59:
        return 'Grade: B+'
    if 60<=s<=69:
        return 'Grade: A'
    if 70<=s<=79:
        return 'Grade: A+'
    if 80<=s<=100:
        return 'Grade: O'

#main
m=float(input('enter math marks: '))
s=float(input('enter science marks: '))
e=float(input('enter english marks: '))
total=m+s+e
avg=total/3
print('\ntotal: ',total)
print('average: ',avg)
print('\nGrades:')
print('Math',grades(m))
print('Science',grades(s))
print('English',grades(e))