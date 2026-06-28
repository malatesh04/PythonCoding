# 1--> without parameter without return value
def mul():
    a = 10;
    b = 20;
    c = a * b;
    print(c)
mul();

#  2--> with parameter without return value
def mul(x,y):
    a = x * y;
    print(a);
mul(10,20);

#  3--> without parameter with return value
def mul():
    a = 10
    b = 20
    c = a * b
    return c
res = mul()
print(res)

#  4--> with parameter with return value
def mul(x,y):
    a = x * y;
    return a;
res = mul(10,20);
print(res)