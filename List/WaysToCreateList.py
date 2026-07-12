# homogenius list
lst = [10,20,30,40,50]
print(lst)
print(len(lst))
print(id(lst))
print(id(lst[0]))

# heteroginius list
lst = [10,20.5,True,1+2j,"python"]
print(lst)
print(len(lst))
print(id(lst))
print(id(lst[0]))

# creating list under another list,tuples,set,distunory
lst = [10,[20,30,40],(50,60,70),{9,10,11},{1:"x",2:"y"}]
# print(lst)
print(lst[0])
print(type(lst[0]))
print(lst[1])
print(lst[1][0]) #taking 0th index of the 1st index
print(type(lst[1]))
print(lst[2])
print(type(lst[2]))
print(lst[3]) #here we can not take index value in set bcz set does not have index values
print(type(lst[3]))
print(lst[4])
print(lst[4][1]) #it gives output you give key value
print(type(lst[4]))


# --> Two operations are happens 1--> concatination 2--> replication
# concatination
lst1 = [10,20,30]
lst2 = [40,50,60]
lst3 = lst1 + lst2
lst4 = lst2 + lst1
print(lst1)
print(lst2)
print(lst3)
print(lst4)

# Replication
lst = [0]*10
print(lst)
lst1 = [1,2,3]*5
print(lst1)

# Slicing
lst = [10,20,30,40,50,60,70]
print(lst)
print(lst[0])
print(lst[::])
print(lst[1:5:])
print(lst[::2])
print(lst[-2:-5:-1])

# reverse a string
s = "malatesh"
print(s[::-1])

# using for iterate the single values in list
lst = [10,20,30,40,50,60]
for i in lst:
    print(i)

# or

lst = [10,20,30,40,50,60]
for i in range(0,len(lst)):
    print(lst[i])