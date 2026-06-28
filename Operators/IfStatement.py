if True:
    print("condition is true")

if False:
    print("condition is true")

n = int(input("enter the number -->"))
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")


# using AND operator

a = int(input("enter 1st num -->"))
b = int(input("enter 2st num -->"))
c = int(input("enter 3st num -->"))

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is gretaer")
    