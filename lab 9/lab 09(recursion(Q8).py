def lenstring(s):
    if s=='':
        return 0
    return 1+lenstring(s[1:])
print(lenstring('vidhi'))   