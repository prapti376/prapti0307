def try1():
    a = int(input("enter first value: "))
    b=  int(input("enter second value: "))
    try:
        c=a/b
        print(c)
    except ZeroDivisionError as zde:
        print("Denominator zero??")
        print(" infinite value")
        print(zde.args)
        x=input("press a key")
        print(zde)

try1()
            