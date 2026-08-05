# import mat
# import test

# mat.mul(10,20)
# test.sum(10,20)

# import math
# print(math.factorial(5))
# print(dir(math))


# exp = input('enter an expression\n')
# res = eval(exp)
# print(res)

# lst = [10,20,30,40,50]
# i = 10
# while i < 100:
#     print(i)
#     i += 10

# def add(x,y):
#     return x+y
# red = add(10,20)
# print(red)

# print((lambda x,y : x+y)(10,20))

# print((lambda num,den : num/den)(20,10))

# lst = [10,13,16,18,19,20]
# def fun(lst):
#     if lst % 2 == 0:
#         return True
#     else:
#         return False
# evn = list(filter(fun, lst))
# print(evn)


# from functools import reduce
# lst = [1,2,3,4,5]
# def fun(x,y):
#     return x+y
# res = reduce(fun,lst) 
# print(res)

# res = reduce(lambda x,y:x+y,lst)
# print(res)


# lst = [1,2,3,4,5]
# def fun(x):
#     return x**2
# res = list(map(fun,lst))
# print(res)

# lst = [1,2,3,4,5]
# print(list(map(lambda x:x**2,[1,2,3,4,5])))