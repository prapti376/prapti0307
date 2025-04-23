#Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if te sum of all the three angles is equal to 180 degrees.


a1 = float(input("Enter the first angle of the triangle: "))
a2 = float(input("Enter the second angle of the triangle: "))
a3 = float(input("Enter the third angle of the triangle: "))


if a1 + a2 + a3 == 180 and a1 > 0 and a2 > 0 and a3 > 0:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")