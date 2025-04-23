#Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.

n = int(input("Enter a number: "))

#Prime
prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

#Perfect number
perfect = sum(i for i in range(1, n) if n % i == 0) == n

#Armstrong
armstrong = sum(int(d)**len(str(n)) for d in str(n)) == n

#Palindrome
palindrome = str(n) == str(n)[::-1]

#Automorphic
automorphic = str(n) == str(n**2)[-len(str(n)):]

print("Prime:", prime)
print("Perfect:", perfect)
print("Armstrong:", armstrong)
print("Palindrome:", palindrome)
print("Automorphic:", automorphic)