# recursive function : the function calls itself

n = int(input("enter the factorial number --> \n"))
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
res = fact(n)
print(res)











