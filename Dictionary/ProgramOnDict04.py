# WAP TO TO PRINT THE MOBILE NUMBER ASSOCIATED WITH THE NAME, IF THE NAME IS NOT AMONG THE ENTRY DISPLAY 'CONTACT NOT FOUND'.
n = int(input())
d = {}

for i in range(n):
    l = input().split()
    d[l[0].lower()] = l[1]

s = int(input())

for i in range(s):
    name = input().lower()
    if name in d:
        print('mob:',d[name])
    else:
        print('No contact found')


# find K'th non repeating value
s = input("enter a string\n").lower()
k = int(input("enter k value\n"))
d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

count = 0

for i in d:
    if d[i] == 1:
        count += 1
        if k == count:
            print(i)
            break
