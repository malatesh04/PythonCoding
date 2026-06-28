# checking prime number using break statement

n = int(input("enter the number\n"))
if n<2:
    print(n,"is not prime")
else:
    for i in range(2,n+1):
        if n%i==0:
            break
    if i==n:
        print(n,"is prime")
    else:
        print(n,"is not prime")