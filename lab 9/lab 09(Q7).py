def ispalindrome(s):
    s2=" "
    for i in s.lower():
        if i == " ":
            continue
        else:
            s2+=i
    print(s==s[::-1])
ispalindrome('aas saa')