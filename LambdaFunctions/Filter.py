# Finding even number in a list.

# using normal def
lst = [10,13,16,18,19,20]
def fun(x):
    if x % 2 == 0:
        return True
    else:
        return False
evn = list(filter(fun, lst))
print(evn)


# using lambda functions
lst = [10,13,16,18,19,20]
evn1 = list(filter(lambda lst : lst%2 == 0, lst))
print(evn1)

# Finding odd number in list
lst = [10,28,36,47,58,96,84,968,94]
odd_num = list(filter(lambda lst : lst%2 != 0,lst))
print(odd_num)

# res = (lambda x, y : x * y)(3,5)
# print(res)

# x = int(input("enter a number --> \n"))
# if (lambda x : x%2 == 0)(x):
#     print(x,"is even")
# else:
#     print(x,"is odd")
