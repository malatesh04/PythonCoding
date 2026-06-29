import math 

# Formate() function --> version 2.6 --> slow in performance 

name = "malatesh"
place = "karjagi"
print("{} {}".format(name,place))
print("{} {}".format(place,name))
print("{:.4f}".format(math.pi))

# 'f' string literal --> version 3.7 --> high in performance

name = "sandeep"
place = "karjagi"
print(f"{name} {place}")
print(f"{place} {name}")
print(f"{math.pi:.4f}")