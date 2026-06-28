# # finding sum of all values present in list

# # using normal def function
from functools import reduce
lst = [1,2,3,4,5]
def func(x,y):
    return x+y
res = reduce(func,lst)
print("the output is -->",res)

# using lambda function
lst = [1,2,3,4,5]
res1 = reduce(lambda  x, y : x+y , lst)
print(res1)


# multiplying all value present in list 
lst = [1,2,3,4,5]
def fun(x,y):
    return x*y
mul_res = reduce(fun,lst)
print(mul_res)

# using lambda function
mul_res1 = reduce(lambda x, y : x * y, lst)
print(mul_res)
