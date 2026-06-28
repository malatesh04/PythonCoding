# where *kargs
# s = {},{},{}.format(*kargs)

s = "{} {} {}".format(10,20,30)
print(s)

s2 = "{2} {0} {1}".format(10,20,30)
print(s2)


# formate specification : additional info : types

# --> 1 alignment types :

# 1--> center
s = "{0:*^11}".format(999) #formate specification --> {index : additional info}
print(s) 

# 2--> Right
s = "{0:*>11}".format(999)
print(s)

# 3--> Left
s = "{0:*<11}".format(999)
print(s)

# --> 2 Presentation types :
import math
s = "{0:.4f}".format(math.pi) #here .f is one type of presentation formate
print(s) #they make here pi is 3.41... you declare how much they cut like 4f --> means only 4 decimal is comes after

s = "{0:10.4f}".format(math.pi)
print(s)

s = "{0:010.4f}".format(math.pi)
print(s)

# 3 exponent type :
earth_weight = 597600000000000000000000
s = "{0:e}".format(earth_weight) # e --> represets exponential of earth weight
print(s)

earth_weight = 597600000000000000000000
s = "{0:.2e}".format(earth_weight) #.2e --> shift 5.9760000 -> 5.97
print(s)

s = "{} {} {}".format([10,20,30]) # here error because have only one argument
print(s)

# overcome this problem --> use list indexing
s = "{0[0]} {0[1]} {0[2]}".format([10,20,30]) 
print(s)

# easy way
s = "{0} {1} {2}".format(*[10,20,30]) # * --> unpacking lis into elements
print(s)
