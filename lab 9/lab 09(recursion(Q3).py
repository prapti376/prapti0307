def count_vowels(s):
    vowels = "aeiou"
    if len(s) == 0:
        return 0
    else:
        if s[0].lower() in vowels:
            return 1 + count_vowels(s[1:])
        else:
            return count_vowels(s[1:])
            
s = input("enter string:")
print(count_vowels(s))