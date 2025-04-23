#Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2'* list (use list comprehension).


l1=[1,2,3,4,5,6,7,8,9,10]
l2=[6,7,8,9,10]

l3=[i for i in l1 if i not in l2]
print(l3)