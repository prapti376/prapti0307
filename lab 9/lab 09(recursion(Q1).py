def primefactors(n,d=2):
    if d>n:
        return None
    if n%d==0:
        print(d)
        return primefactors(n//d,d)
    return primefactors(n,d+1)
num = int(input("enter a number:"))
primefactors(num)

    