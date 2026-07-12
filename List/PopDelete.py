#POP FUNCTION -->

lst = [10,20,30,40,50,60]
print(lst)
lst.pop() # don't give index in pop they remove last element in the list
print(lst)
lst.pop(2) # you give index in pop then they remove whatever you give idex that element is remove
print(lst)

# DEL FUNCTION -->

lst = [10,20,30,40,50,60,70,80,90,100]
print(lst)
del lst[3] # delete 3rd index of list
print(lst)
del lst[2:7] #delete the specific porsion
print(lst)
del lst[::2] #delete alternative  
print(lst)
del lst[-4:-9:-1]
print(lst)

# deletion of element
# > based on values --> remove()
# > based on index --> pop(), del 
