#24 hrs of day with am, pm, midnight, noon
for i in range(24):
    if i==0:
        print(i,"midnight")
    if i<12 and i!=0:
        print(i,"am")
    if i==12:
        print(i,"noon")
    if i>12:
        print(i,"pm")