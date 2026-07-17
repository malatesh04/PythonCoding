# WAP TO COUNT THE OCCURENCE OF EACH CHARACTER IN THE GIVEN STRINGS.
s = 'MISSISSIPPi'.lower()
d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
print(d)

# WAP TO COUNT THE OCCURENCE WHERE CHARACTER > 3 IN THE GIVEN STRINGS.
s = 'MISSISSIPPi'.lower()
d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
for i in d:
    if d[i]>3:
        print(i)

# WAP TO COUNT THE TOTAL NUMBER OF PAIRS.
lst = map(int,input().split())
d = {}
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

res = 0

for i in d.values():
    res += i//2
print(res)


#FIND THE NUMBER OF OCCURENCE IN YOUR NAME

s = input("enter a string\n").lower() 
d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
for i,j in d.items():
    print(i,j)