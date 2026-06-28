# Variable Length Arguments --> called Arbitrary Arguments

def pizza(*Toppings): #when you give '*' then they collect variable length arguments
    print(Toppings)
    print(type(Toppings))
pizza("cheese","tomato","onion")

# '*' --> used to indicate to python this is such a parameter 
# which is capable of accepting variable length argumnets

# --> internally python is collected all arguments stored it 
# in toppings and toppings is a tuple.


# Rules:

# here you give one variable length arguments and next one anotehr 
# argument in parameter now when u give input to parameter as 
# argument whatever u give that all are treated as variable length 
# argument all are stored in *Toppings only you give the input to 
# crust then  you use "Keyword arguments".

def pizza(*Toppings,crust): #crust you declare in keyword argument
    print(Toppings)
    print(crust)
    print(type(Toppings))
pizza("cheese","onion","tamato",crust="thin")

# now :
def pizza(name,*Toppings,crust): # here before variable argument don't need give keyword arguments
    print(name)
    print(Toppings)
    print(crust)
pizza("malatesh","cheese","onion","tamato",crust="thin")

