lst = [10,20,30,40,50]
for i in [60,70,80]:
    lst.append(i)
print(id(lst))

for i in [90,100]:
    lst.append(i)
print(id(lst))

for i in [110,120]:
    lst.append(i)
print(id(lst)) 

lst = [10,20,30,20,30,40,20,30,20]
count = 0

for i in lst:
    if i==20:
        count = count+1
print(count)
