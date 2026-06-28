lst = [1,2,3,4,5]

# using def keyword
def fun(x):
    return x**2;
res = list(map(fun,lst))
print(res)

# using lambda keyword
print(list(map(lambda x : x**2,lst )))

# def funtion under lambda function

def fun1(num):
    return (lambda x : x*num)
res = fun1(2)(5)
print(res)

# multiplication
v = int(input("enter multiplication value --> \n"))
def fun(num):
    return lambda x : x*num
math_table = fun(v)

for i in range(1, 11):
    print(f"{v} X {i} = {math_table(i)}")
    i = i+1; 