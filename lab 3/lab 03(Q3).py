#Accept two strings. Check whether one string is there in another string.

s1=input("enter the first string:")  
s2=input("enter the second string:")  

if s1 in s2:
    print("'{s1}' is present in '{s2}'")
elif s2 in s1:
    print("'{s2}' is present in '{s1}'")
else:
    print("Neither string is a substring of the other.")