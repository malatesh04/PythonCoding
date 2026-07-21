def fun():
    print('hello world')
fun()
print(fun)
print(fun())
fun2 = fun
print(fun2)

# two functions are there one is refering to another
def alpha(ref):
    print('inside alpha()')
    ref()
def beta():
    print('inside beta()')
alpha(beta)


def get_sum(lst):
    print(sum(lst))
def get_product(lst):
    p = 1
    for i in lst:
        p = p*i
    print(p)
def fun(choice):
    if choice == 'sum':
        return get_sum
    elif choice == 'product':
        return get_product
fun1 = fun('sum')
fun1([10,20,30])
fun2 = fun('product')
fun2([10,20,30,40])


#here do not call inner function out side the function. 
def outer():
    print('inside outer()')
    def inner():
        print('inside inner()')
    inner()
outer()

# thats why use this way
def outer():
    print('inside outer()')
    def inner():
        print('inside inner()')
    return inner
in_ref = outer()
in_ref()

# DECORATORS -->

# here one function is defined but i don't want to modify them add another function then ref that function.
def outer(ref):
    def wrapper(lst):
        if 0 in lst:
            print('0 is present')
        else:
            ref(lst)
    return wrapper

@outer
def get_product(lst):
    p = 1
    for i in lst:
        p = p*i
    print(p)

# modified_get_product = outer(get_product)
# modified_get_product([10,20,30])
# modified_get_product([10,0,30])
get_product([10,20,30])
get_product([10,0,30])

# without decorator
def outer(ref):
    def wrapper(a,b):
        if b == 0:
            print('plz provide non zero denominator')
        else:
            ref(a,b)
    return wrapper 
def div(a,b):
    print(a/b)
mod_div = outer(div)
mod_div(10,2)
mod_div(10,0)

# with decorator
def outer(ref):
    def wrapper(a,b):
        if b == 0:
            print('plz provide non zero denominator')
        else:
            ref(a,b)
    return wrapper 
@outer
def div(a,b):
    print(a/b)
div(10,2)
div(10,0)