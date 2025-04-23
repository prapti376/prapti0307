import math
def sm():
    n=int(input("enter a number:"))
    r=int(input("input comman diff: "))
    print("ncr", math.factorial(n)/math.factorial(n-r))
    print("pcr", math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

sm()