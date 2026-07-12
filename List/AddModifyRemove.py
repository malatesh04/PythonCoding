lst = [10]
print(lst)
print(id(lst))
lst.append(20)
print(lst)
print(id(lst))

# MUTABILITY --> any list can be add,remove,modify than called mutable in nature

# ADD--> 

lst = [10,20,30,40,50]
print(lst)
lst.append(60)
print(lst)
# multiple elemts to add
lst.append([70,80,90]) #here the other list is created 6th index --> but i don't want want that list 
print(lst)
# --> 1st approch
lst = lst + [70,80,90]
print(lst)
# --> 2nd approch
lst.extend([1,2,3])
print(lst)

# INSERSION -->

lst = [10,20,30,40,50]
print(lst)
lst.insert(2,[25])
print(lst)

# Replacing elememts in list
lst = [10,20,30,40,50]
print(lst)
lst[2] = 300
print(lst)

# Replacing elements 20,30,40 to 99
lst = [10,20,30,40,50]
print(lst)
lst[1:4] = [99]
print(lst)

# or 

lst = [10,20,30,40,50]
print(lst)
lst[1:4] = [99,98,97]
print(lst)

lst = [10,20,30,40,50]
print(lst)
lst[::2] = [99,98,97]
print(lst)

# REMOVE -->

# having only one 30 in list
lst = [10,20,30,40,50]
print(lst)
lst.remove(30)
print(lst)

# having 2 30 in list
lst = [10,20,30,40,50,30]
print(lst)
lst.remove(30) #always remove 1st 30
print(lst)

# membership present check
lst = [10,20,30,40,50]
print(30 in lst)

# membership absent check
lst = [10,20,30,40,50]
print(30 not in lst)

# removing all 30 in list
lst = [10,20,30,40,50]
 
while 30 in lst:
    lst.remove(30)
print(lst)
