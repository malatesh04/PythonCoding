#  --> exapme is list

lst = [10, 20, 30, 40, 50]
print(lst)
print(id(lst))

lst.append(60)
print(lst)
print(id(lst))

list = [10, 20, 30, 40, 50, 60]
print(id(list))

print(list is lst)
