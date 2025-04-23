#Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) ).


import math

def check_position(cx, cy, r, px, py):
    d = math.sqrt((px - cx)**2 + (py - cy)**2)

    if d < r:
        print("Inside the circle.")
    elif d == r:
        print("On the circle.")
    else:
        print("Outside the circle.")


cx = float(input("Enter circle center x: "))
cy = float(input("Enter circle center y: "))
r = float(input("Enter radius: "))
px = float(input("Enter point x: "))
py = float(input("Enter point y: "))


check_position(cx, cy, r, px, py)