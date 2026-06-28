#  --> compare using values --> ==
#  --> compare refereces of a string --> id() function or is operator
#  --> 

s1 = "python"
s2 = "java"
if s1 == s2:
    print("string values are equal")
else:
    print("strings values are unequal")


s1 = "PYTHON"
s2 = "python"
print(s1 is s2)
print(id(s1[0]))
print(id(s2[0]))


s1 = "python"
s2 = "java"
if id(s1) == id(s2):
    print("string references are equal")
else:
    print("strings references are unequal")


s1 = "python"
s2 = "python"
if s1 == s2:
    print("string values are equal")
else:
    print("strings values are unequal")


s1 = "python"
s2 = "python"
if print(id(s1)) == print(id(s2)):
    print("string references are equal")
else:
    print("strings references are unequal")


s1 = "python"
s2 = "python"
if s1 is s2:
    print("string references are equal")
else:
    print("strings references are unequal")


s1 = "python"
s2 = "PYTHON"
if s1 == s2:
    print("string values are equal")
elif s1 is s2:
    print("string values are equal")
elif id(s1) is id(s2):
    print("string values are equal")
else:
    print("strings values are unequal")