# in function we can return multiple values

def fun():
    a = 10
    b = 20
    c = 30
    return a,b,c
res = fun() # packed values in tuple
print(type(res))
print(res)

# unpacking values
def fun():
    a = 10
    b = 20
    c = 30
    return a,b,c
res1,res2,res3 = fun() # unpacking values by variables
print(res1)
print(res2)
print(res3)