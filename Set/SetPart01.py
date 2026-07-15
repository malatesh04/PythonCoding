# set --> unordered set --> hash functions only decide the order
set = {18,45,95,88,30,23,54,41,80,65,92}
print(id(18))
print(id(45))

# set -> unorderd --> not allow duplicate --> allow only mutable data
s = {95, 45, 160, 80, 20, 66, 88, 15, 15, 65, 22}
print(s)
print(s)

# take mutable and not mutable data types both
s = {10, 3.14, True, 1+3j, (40, 50, 60), "Python"}
print(s)

# not take mutable data structure
s = { [10, 20, 30], {66, 77, 88}, {1: 'A', 2: 'B'} }
print(s)

# mutable in nature
s = {10,20,30,40,50}
print(s)
s.add(999)
print(s)
s.remove(999)
print(s)
s.pop()
print(s)
s.pop()
print(s)

s = {10,20,30,40,50}
print(s)
# s.remove(99) #here error is occurese bcz not there 
s.discard(99) #overcome error
print(s)

