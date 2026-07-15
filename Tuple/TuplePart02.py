t = (10,20,30,40)
print(t)
t.append(99)
print(t)

# in tuple everything is object
t = [10,20,30,40]
print(id(t))
print(id(0))
print(id(1))
print(id(2))
print(id(3))

# in tuple store empty 
tup = ()
print(tup)

# using tuple function create empty tuple
tup = tuple()
print(tup)

# create homogenius elements in tuple
tup = (10,20,30,40,50)
print(tup)

# create heterogenius elemets in tuple
tup = (10,26.7,True,1+3j,"python")
print(tup)

# creating int,list,tuple,dict,set in tuples
tup = (10,[20,30],(40,50),{60,70},{"name":"malatesh","age":10})
print(tup)
print(tup[1][0])
print(tup.append(99))

# CHECK TUPLE IS IMMUTABLE IN NATURE
tup = (10,[20,30],(40,50),{60,70},{"name":"malatesh","age":10})
print(tup.append(99))
print(tup.extend((99,98)))
print(tup.insert(2,20))
tup[0] = 20
print(tup.pop())
print(tup.pop(2))
print(tup.remove())
print(tup.remove(10))
print(tup[1])
print(tup[1:4:])

tup = (10)
print(tup)
print(type(tup))

tup = (10,)
print(tup)
print(type(tup))

tup = 10,20,30
print(tup)
print(type(tup))