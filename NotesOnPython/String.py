s = input('enter the string\n')

for i in range(0,len(s)-2):
    print(s[i:i+3])

print(s[1:-1])

s = input('enter the string\n')
s_upper = ''

for i in s:
    if ord(i)>=97:
        s_upper = s_upper + chr(ord(i)-32)
    else:
        s_upper = s_upper + i
print(s)
print(s_upper)

lst = ['Python','Java','Django','Spring']
s = ''
for i in lst:
    s = s+i
print(s)

lst = ['Python','Java','Django','Spring']
s = "".join(lst)
print(s)


url = [
    "https://www.google.com/",
    "https://www.youtube.com/",
    "http://www.xyz.com",
    "http://www.abc.org"
]
for i in url:
    if i[len(i)-3:] == "com" or i[len(i)-4:] == "com/":
        print(i)
    print(len(i))

s = "Error 404 not found"

# table = s.maketrans("aeiou", "AEIOU", "0123456789")

s_table = s.translate("aeiou", "AEIOU", "0123456789")

print(s)
print(s_table)