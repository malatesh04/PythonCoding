# 10 is object they store in private heap memory segment and 
# a is variable is store in stack segment in heap they take 
# on memory address and refer to one varible present in stack.

a = 10
print(a)
print(id(a)) #id function --> to find address of the object

a = 20
print(a) 
print(id(a)) #id function --> to check address of the object

print(a is a)


# onneka 10 a varible assign agitt amele 20 na b anno variable 
# save madidra avaga a anno variable first address bitt second 
# address gee refer madutt avaga first addredss kali erutta adna 
# python no use andu garbage collector adna collect madutt avaga 
# a next 20 ge refer madutt 

# --> when two variable name is same but object is different
# then two object are created but one first object is not refering 
# any more then garbage collector take it the second varible is refering 
# to object