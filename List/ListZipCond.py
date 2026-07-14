lst1 = ['A','app','','da','kee','t','doc','a']
lst2 = ['n','le','a','y','ps','he','tor','way']
res = []

for i,j in zip(lst1,lst2):
    res.append(i+j) 
print(' '.join(res))


# one line
print(' '.join([i+j for i,j in zip(['A','app','','da','kee','t','doc','a'],['n','le','a','y','ps','he','tor','way'])]))

s = input("enter a string\n")
lst = s.split()
res = []
for i in range(len(lst)):
    if len(lst[i]) > 5:
        res.append(lst[i].lower())
    else:
        res.append(lst[i].upper())
print(' '.join(res))

print(' '.join([lst[i].lower() if len(lst[i]) > 5 else lst[i].upper() 
for i in range(len(lst))]))