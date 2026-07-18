# WAP TO COUNT THE OCCURENCE OF EACH WORD IN THE GIVEN SENTENCE.
import re
s = input().upper()
s = re.sub(r'[.,?!]',' ',s)
lst = s.split()
d = {}
count = 0
for i in lst:
    if i not in d:
        d[i] = 1
        count += 1
    else:
        d[i] += 1
        count +=1
print(d)
print(count) 


d = {1:'A',2:'B',3:'A',4:'B',5:'B',6:'C'}
res = {}

for i in d:
    if d[i] not in res:
        res[d[i]] = []
        res[d[i]].append(i)
    else:
        res[d[i]].append(i)
print(res)