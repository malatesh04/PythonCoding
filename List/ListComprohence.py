# if else in compreshension

# PROGRAMM 01 : in list which is even square and odd make add 

lst = [3,6,5,4,2]
even_add = []
odd_sq = []

for i in lst:
    if i%2 == 0:
        even_add.append(i+i)
    else:
        odd_sq.append(i**2)
print(even_add)
print(odd_sq)

# given list make which is even make square, which is odd make add.
# Traditional way
lst = [3,6,5,4,2]
res = []

for i in lst:
    if i%2==0:
        res.append(i*i)
    else:
        res.append(i+i)
print(res)

# list compruhension
lst = [3,6,5,4,2]
res = [i*i if i%2==0 else i+i for i in lst]
print(lst)
print(res)
# --> (want u want if condition else what u want loop)
# when both if and else in program
# --> (expression if condition else expression loop)
# when only if in program
# --> (expression loop if condition)


# PROGRAM 2 : PROGRAM TO COUNT THE NUMBER OF VOWELS
text = input("enter a string\n").strip().lower()
vowels = "aeiouAEIOU"
count = 0
res = []
for i in text:
    if i in vowels:
        res.append(i)
        count = count+1
print(count)
print(res)

text = input("enter a string\n").strip().lower()
vowels = "aeiou"
print(len([i for i in text if i in vowels]))

# or --> one line program
print(len([i for i in input("string\n") if i in "aeiouAEIOU"]))


# PROGRAM 3 : TO FIND PAIRS FROM 2 LIST 

# Traditional method
lst1 = [2,4,3]
lst2 = [5,2,4,1]
lst3 = []
for i in lst1:
    for j in lst2:
        if i!=j:
            lst3.append((i,j))
print(lst3)

# list comprohenses
print([(i,j) for i in [2,4,3] for j in [5,2,4,1] if i!=j])


# PROGRAMM 04 : PRINT THE NUMBER AND ITS CUBE TILL N
n = int(input("enter a N:"))
res = []
for i in range(1,n+1):
    res.append((i,i**3))
print(res)

# one line :
print([(i,i**3) for i in range(1,int(input("enter a N:"))+1)])