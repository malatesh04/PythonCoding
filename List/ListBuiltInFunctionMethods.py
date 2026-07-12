# Functions -->

lst = [10,20,30,40,50]

# Length Functions
print(len(lst))

# Max Function
print(max(lst))

# Min Function
print(min(lst))

# Sum Function
print(sum(lst))

# Range Function
for i in range(len(lst)):
    print(i,lst[i])

# Enumarate Function
for i,j in enumerate(lst):
    print(i,j)

# Methods --> 

lst = [10,20,30,40,50,20]

# Count Method
print(lst.count(20))

# Index Method
print(lst.index(20)) # gives first occurence.
print(lst.index(200)) # value error --> 200 not in list
print(lst.index(20,2,6)) # (object,start,stop)

# Clear Method
print(lst)
lst.clear() # none
print(lst)

# Sorting --> arrenging ascending or descending order
lst = [25,17,36,7,55,13]
print(lst)

# Ascending order using Function
lst = sorted(lst,reverse=False) # using function brand new list is created old list not have any references then memory deallocate they go garbage collector collect that list
print(lst)

# Descending order Function
lst = sorted(lst,reverse=True)
print(lst)

# Sorting using method called sort

# Ascending Order
lst.sort(reverse=False) # In methods when sorting happens there is no new list created in that they sort happens.
print(lst) 

# Descending Order
lst.sort(reverse=True)
print(lst) 

# Reverce using Function
lst_rev = list(reversed(lst))
print(lst_rev)

# Reverse using method
lst.reverse()
print(lst)

# Programs -->

# 1) PROGRAM TO FIND THE SUM OF SUBLIST --> 
lst = input("enter the list []\n")
lst = eval(lst) #convert string into list
start = int(input("Enter the start index\n"))
stop = int(input("Enter the stop index\n"))
print("Sum =",sum(lst[start:stop+1]))

# 2) PROGRAMM TO APPEND THE ELEMENTS WHICH IS NOT PRESENT IN THE PRIMARY LIST
lst1 = eval(input("enter the list 1[]\n"))
lst2 = eval(input("enter the list 2[]\n"))

for i in lst2:
    if i not in lst1:
        lst1.append(i)
print(lst1)

