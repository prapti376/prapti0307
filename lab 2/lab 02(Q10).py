#Given the length and breadth of a rectangle, write a program to find whether the are of the rectangle is greater than its perimeter
l=float(input('enter length of rectangle: '))
b=float(input('enter breadth of rectangle: '))
p=2*(l+b)
a=l*b
if a>b:
    print('area of rectangle is greater than perimeter')
else:
    print('area of rectangle is smaller than perimeter')