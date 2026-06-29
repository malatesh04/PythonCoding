# user give input numbers like --> 12 14 18 22 26
# output --> Avg = 18.4000 --> exactly 4 decimal points are come

nums = input("enter a numbers\n").split()
print(nums)  # in string 
# print(type(nums))
l = list(map(int,nums)) # convert string into int using map function
print(l)

from functools import reduce
res = reduce(lambda x,y : x+y,l)
Avg = res/len(l)
# print(Avg)
print("{0:^14.4f}".format(Avg))