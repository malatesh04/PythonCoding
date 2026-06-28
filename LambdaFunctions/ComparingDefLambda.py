# example --> to find power

# using def keyword 
def power_of(num,p):
    return num**p
res = power_of(2,5)
print(res)

# using lambda keyword --> one line function, single/one time use functions
# syntax : (lambda arguments : expression)(input)

res1 = (lambda num,p : num**p)(3,2)
print(res1)


# example 2 --> to find quotient 

def get_quotient(num,den):
    return num/den
res = get_quotient(10,2)
print(res)

res1 = (lambda num,den : num/den)(11,3)
print(res1)

# but i want to call now 

fun = lambda num,den : num/den
print(fun(12,3))
print((fun)(12,5))
