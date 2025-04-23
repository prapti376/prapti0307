#Count how many vowels are there in a string. Accept the string from the user.

s1=input("enter the string:")  
vowels= "aeiouAEIOU"
count = 0
for ch in s1:
    if ch in vowels:
         count=count+1

print("No. of vowels in s1:",count)