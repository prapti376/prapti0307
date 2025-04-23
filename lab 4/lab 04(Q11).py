#Calculate sin(x); x is a radian value. The formula is as under: sinx = x-x3/3! + x5/5! - x7/7!... 



def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

x = float(input()) * (3.14159 / 180)  # Convert degrees to radians
s = 0  

for i in range(5):  # Using 5 terms for simplicity
    s += ((-1) ** i) * (x ** (2 * i + 1)) / fact(2 * i + 1)

print(s)