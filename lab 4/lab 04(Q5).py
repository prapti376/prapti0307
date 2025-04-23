#Generate all Pythagorean Triplets with side length <= 30.

for a in range(1, 31):
    for b in range(a, 31):
        c = (a**2 + b**2) ** 0.5
        if c == int(c) and c <= 30:
            print(a, b, int(c))