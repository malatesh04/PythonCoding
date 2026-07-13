lst = eval(input("enter a list between []\n").strip())
larg = lst[0]

for i in lst:
    if i>larg:
        larg = i
print("largest number -->",larg)