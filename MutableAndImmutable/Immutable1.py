# when variable name is different but object is same 
#  --> in heap segment only one object is created but two variable are refering to taht address

a = 10
print(a)
print(id(a))

b = 10
print(b)
print(id(b))

print(a is b)