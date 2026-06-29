# b --> decimal to binary
# o --> decimal to octal
# x --> decimal to hexadecimal

# converting decimal into binary
a = 70
print(a)
print("{0:b}".format(a)) # convert decimal --> binary
print("{0:o}".format(a)) # convert decimal --> octal
print("{0:x}".format(a)) # covert decimal --> hexadecimal 

# using f formate()
a = 70
print(a)
print(f"{a:b}")
print(f"{a:o}")
print(f"{a:x}")