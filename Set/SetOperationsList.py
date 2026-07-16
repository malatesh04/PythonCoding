s1 = {}
s2 = {}

# 1. Union
s1 | s2
s1.union(s2)

# 2. Intersection
s1 & s2
s1.intersection(s2)

# 3. Difference
s1 - s2
s1.difference(s2)

# 4. Symmetric Difference
s1 ^ s2
s1.symmetric_difference(s2)

# 5. Subset
s1 <= s2
s1.issubset(s2)

# 6. Superset
s1 >= s2
s1.issuperset(s2)

# 7. Disjoint Set
s1.isdisjoint(s2)