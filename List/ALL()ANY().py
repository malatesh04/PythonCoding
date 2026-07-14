lst = [-1,20,30,40,50]
lst2 = []
for i in lst:
    if i > 0:
        lst2.append(True)
    else:
        lst2.append(False)
print(all(lst2))
print(any(lst2))

print(all([True if i > 0 else False for i in [-1,20,30,40,50]]))
print(any([True if i > 0 else False for i in [-1,20,30,40,50]]))



# ALL() FUNCTION -->
marks = [45,75,30,80,95,65]
print(all([i>35 for i in marks ]))

# ANY FUNCTION -->
marks = [45,75,30,80,95,65]
print(any([i>70 for i in marks ]))


