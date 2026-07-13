# PROGRAM TO INSERT AN ELEMENT AT RIGHT POSITION WITHIN SORTED LIST

lst = eval(input("enter a sorted list between []\n"))
n = int(input("enter the number\n"))
print(lst)

for i in range(len(lst)):
    if n<lst[i]:
        lst.insert(i,n)
        break

print(lst)














