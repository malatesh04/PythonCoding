# SUBSET OPERATION -->
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {3,11,4,7}
print(s2 <= s1) # operator
print(s2.issubset(s1)) # method

# SUPERSET OPERATION -->
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {3,11,4,7}
print(s1 >= s2) # operator
print(s1.issuperset(s2)) # method

# DISJOINT OPERATION -->
s1 = {1,2,3,4,5,6,7,8,9,10,11,13}
s2 = {20,30,40,50}
print(s1.isdisjoint(s2)) # only method

# WRITE A PROGRAM TO TAKE PROGRMMING NAME AND REMOVE DUPLICATES.
lst = input().split()
print(lst)
print(set(lst))

# WAP TO PRINT THE NUMBER OF DUPLICATES ELEMENTS IN LIST
lst = input("emter a list\n").split()
s = set(lst)
print(len(lst)-len(s))


h = {1,9,12,7,14}
f = {6,9,8,10,5,11,12,13,15}
c = {2,4,9,3,5,13}
print(f"all roll number: {h | f | c}")
print(f"common player: {h & f & c}")
print(f"only hokey: {h-(f|c)}")
print(f"not common player: {f^c}")