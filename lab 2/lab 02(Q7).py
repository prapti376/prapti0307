#Accept a year value from the user. Check whether it is a leap year or not

def leap(x):
    if x%400==0:
        print('leap year')
    elif x%4==0 and x%100!=0:
        print('leap year')
    else:
        print('not leap year')

x=int(input('enter a year: '))
leap(x)