import random
numbers = { random.randint(15,45) for i in range(10) }
count = sum(1 for num in numbers if num<30)
s1={i for i in numbers if i<36}
print(numbers)
print(count)
print(s1)
