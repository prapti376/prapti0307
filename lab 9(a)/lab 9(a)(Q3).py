import random
l=[random.randint(-15,15) for i in range(10)]
print(l)
m=list(map((lambda x:x**2),l))
print(m)