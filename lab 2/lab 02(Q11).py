#Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line
x1,y1=1,2
x2,y2=3,4
x3,y3=5,6
if ((x2-x1)/(y2-y1))==((x3-x1)/(y3-y1)):
    print('points are collinear')
else:
    print('points are not collinear')