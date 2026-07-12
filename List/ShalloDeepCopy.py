#  --> two ways to copy the list

# 1st way --> using slicing. 
lst1 = [10,20,30,40,50]
lst2 = lst1[::]
print(lst1)
print(lst2)
print(lst1 is lst2)

# 2nd way --> using list function.
lst1 = [10,20,30,40,50]
lst2 = list(lst1)
print(lst1)
print(lst2)
print(lst1 is lst2)

# nested list to copy --> shallow copy
lst1 = [[10,20],[30,40]]
lst2 = lst1[::]
print(lst1)
print(lst2)
print(lst1 is lst2)
lst1.append([50,60])
print(lst1)
print(lst2)
lst1[1][0] = 333
print(lst1)
print(lst2)

# nested list to copy --> deep copy
import copy
lst1 = [[10,20],[30,40]]
lst2 = copy.deepcopy(lst1)
print(lst1)
print(lst2)
print(lst1 is lst2)
lst1.append([50,60])
print(lst1)
print(lst2)
lst1[1][0] = 333
print(lst1)
print(lst2)