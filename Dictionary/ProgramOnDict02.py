d = {1: 'a', 2: [10, 20, 30]}

print(d[1])
x = d[1]
print(x)
x = 'b'
print(d[1])
print(x)
# Print the list stored at key 2
print(d[2])
# Store the reference of the list in variable lst
lst = d[2]
print(lst)
# Add a new element to the list
lst.append(99)
# Since lst and d[2] refer to the same list,
# the dictionary value is also updated
print(d[2])
# Print the updated list
print(lst)


# POWERFULL METHODS
'''keys --> keys()
values --> values()
items --> items()'''

d = {1:'c',2:'java',3:'python'}
print(list(d.keys()))
for i in d.keys():
    print(i,d[i])

d = {1:'c',2:'java',3:'python'}
print(list(d.values()))
for i in d.values():
    print(i)

d = {1:'c',2:'java',3:'python'}
print(list(d.items()))
for i in d.items():
    print(i)

d = {1:'c',2:'java',3:'python'}
print(list(d.items()))
for i,j in d.items():
    print(i,j)