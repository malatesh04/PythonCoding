# Create a set
s = {100, 20, 12, 22, 41, 33, 52, 80, 73}

# 1. Add an element
s.add(45)
print("After add:", s)
# Time Complexity: O(1)

# 2. Remove an element
s.remove(45)
print("After remove:", s)
# Time Complexity: O(1)

# 3. Pop an arbitrary element
removed = s.pop()
print("Popped element:", removed)
print("After pop:", s)
# Time Complexity: O(1)

# 4. Membership test
print(33 in s)
# Time Complexity: O(1)



# Set 1
s1 = {1, 2, 3, 4, 5, 6, 8, 10, 11, 13}

# Set 2
s2 = {7, 9, 14, 15, 16, 22, 77, 86}

print("Set 1:", s1)
print("Set 2:", s2)

# 1. Union
print("\nUnion")
print(s1 | s2)
print("Time Complexity: O(n1 + n2)")

# 2. Intersection
print("\nIntersection")
print(s1 & s2)
print("Time Complexity: O(n1 + n2)")

# 3. Difference
print("\nDifference (s1 - s2)")
print(s1 - s2)
print("Time Complexity: O(n1 + n2)")

# 4. Symmetric Difference
print("\nSymmetric Difference")
print(s1 ^ s2)
print("Time Complexity: O(n1 + n2)")


# Set 1
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13}

# Set 2
s2 = {3, 4, 7, 11}

# Set 3 (Disjoint Set)
s3 = {18, 19, 20, 56}

print("Set 1:", s1)
print("Set 2:", s2)
print("Set 3:", s3)

# 1. Subset
print("\nSubset")
print(s2 <= s1)
print(s2.issubset(s1))
print("Time Complexity: O(n2)")

# 2. Superset
print("\nSuperset")
print(s1 >= s2)
print(s1.issuperset(s2))
print("Time Complexity: O(n2)")

# 3. Disjoint Set
print("\nDisjoint Set")
print(s1.isdisjoint(s3))
print("Time Complexity: O(n1 + n2)")