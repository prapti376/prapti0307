#Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.


def to_lower(s):
    res = ""
    for c in s:
        if 'A' <= c <= 'Z':
            res += chr(ord(c) + 32)
        else:
            res += c
    return res

def to_upper(s):
    res = ""
    for c in s:
        if 'a' <= c <= 'z':
            res += chr(ord(c) - 32)
        else:
            res += c
    return res

def to_toggle(s):
    res = ""
    for c in s:
        if 'A' <= c <= 'Z':
            res += chr(ord(c) + 32)
        elif 'a' <= c <= 'z':
            res += chr(ord(c) - 32)
        else:
            res += c
    return res

s = input()
print(to_lower(s))
print(to_upper(s))
print(to_toggle(s))