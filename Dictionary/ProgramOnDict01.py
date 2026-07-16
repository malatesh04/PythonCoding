d = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'6'}
d.pop(3) #pop whatever u give key value
d.popitem() # pop last item
del d[1] # using del keywords
d.pop(99) # here they give keyerror bcz 99 not in dictionary
print(d.pop(99,'notfound')) #thats why use "not found" --> in pop() method 
d.clear() # all clear in dictinary
print(d)
