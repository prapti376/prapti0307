def try1():
    try:
        x=int(input("enter a integer: "))
    except ValueError as ve:
        print(ve)
        print("try again\n")
        try1()
try1()
        
        