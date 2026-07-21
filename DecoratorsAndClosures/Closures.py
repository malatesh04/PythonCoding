def outer(ref):
    def wrapper(lst):
        if 0 in lst:
            print('zero in list')
        else:
            ref(lst)
    return wrapper
@outer
def product(lst):
    p = 1 
    for i in lst:
        p = p*i
    print(p)
product([10,0,30])
product([10,20,30])

def decorator(num):
    def power_of(ref):
        def wrapper(lst):
            lst = list(map(lambda x:x**num,lst))
            ref(lst)
        return wrapper
    return power_of
@decorator(2)
def product(lst):
    p = 1 
    for i in lst: 
        p = p*i
    print(p)
fun1 = decorator(3)
fun2 = fun1(product)
fun2([1,2,3,4,5])

# closures --> here del outer is written means outer gets garbage and x = 10 also vanished 
# --? but using clousers the whatever is stored in variable they are excessable
def outer():
    x = 10
    def inner():
        print(x)
    return inner
fun = outer()
del outer
fun()


def outer():
    x = 99
    def inner1():
        y = 88
        def inner2():
            print(x)
            print(y)
        return inner2
    return inner1
fun1 = outer()
fun2 = fun1()
fun2()
del outer
del fun1
fun2()