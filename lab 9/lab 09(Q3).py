def create_array(a,b,c,d):
   array=[[[d for _ in range(a)]for _ in range(b)]for _ in range(c)]
   return array

array_3d = create_array(2,3,4,1)
for layer in array_3d:
    for row in layer:
          print(row)
    print()
    