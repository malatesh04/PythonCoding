print("enter numerator")
num = int(input())
print("enter denominator")
den = int(input())

res = int(num/den)
print(res)

# or

numerator = int(input("enter the numerator -->\n ")) #\n --> new line 
denominator = int(input("enter the denominator -->\n "))
def fun():
    res = int(numerator/denominator)
    print(res)

fun()


# eval funtion

exp = input("enter expression\n")
res = eval(exp) #evaluate expression whatever user given 
print(exp)
print(res)