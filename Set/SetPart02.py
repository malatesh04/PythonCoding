# 1--> union operation
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1|s2) # using operator
print(s1.union(s2)) # using union() method

# 2 --> intersection operation
s1 = {1,2,3,4,5,6,7,8}
s2 = {1,2,3,6,8,9}
print(s1 & s2) # using '&' operator
print(s1.intersection(s2)) # using intersection() method

# 3 --> difference operation
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1 - s2) # using opeartor
print(s1.difference(s2)) # using method
print(s2 - s1) # using opeartor
print(s2.difference(s1)) # using method

# 4--> symmetric difference --> union - intersection
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1 ^ s2) # using opeartor
print(s1.symmetric_difference(s2)) # using method

# cool method --> 1--> 

# before
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1)
print(s1.intersection(s2))
print(s1)

# after
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1)
print(s1.intersection_update(s2))
print(s1)

# 2--> # before
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1)
print(s1.difference(s2))
print(s1)

# after
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1)
print(s1.difference_update_update(s2))
print(s1)

# 3--> 
# before
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1)
print(s1.symmetric_difference(s2))
print(s1)

# after
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {7,9,10,77,14,15,16,22,86}
print(s1)
print(s1.symmetric_difference_update(s2))
print(s1)