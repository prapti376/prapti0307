#Print largest and smallest values out of two

n1 = int(input("Enter first number: ")) 
n2 = int(input("Enter second number: ")) 

if n1 > n2:
    largest = n1
    smallest = n2
else:
    largest = n2
    smallest = n1

print("The largest number is:", largest)  
print("The smallest number is:", smallest)