#Generate N numbers of Fibonacci series.

n = int(input())  
a, b = 0, 1  

for _ in range(n):  
    print(a)  
    a, b = b, a + b  