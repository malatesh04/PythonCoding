s = input("enter the string\n").strip()
freq = {}

for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for i,count in freq.items():
    print(i,count)