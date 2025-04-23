def revlist(lst):
    if lst:
        return revlist(lst[1:]) +[lst[0]]
    return lst

lst= [1,2,3,4,5]
print("original list" ,lst)
print("reversed list" ,revlist(lst))