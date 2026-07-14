lst1 = [5,12,15,7]
lst2 = [15,8,15,3]
lst3 = list(zip(lst1,lst2))
print(lst3)

# one line
print(list(zip([5,12,15,7],[15,8,15,3])))

lst1 = [5,12,15,7]
lst2 = [15,8,15,3]
for i,j in zip(lst1,lst2):
    print(i,j)