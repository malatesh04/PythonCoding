import re
text = '''malatesh@gmail.com
malatesh@@gmail.com
malatesh@4gmail.com
malatesh178@gmail.com
malatesh@yahoo.com
malatesh@outlook.com'''
regex = r"[a-zA-Z0-9_$\-]+@[a-zA-Z]+.com"
match = re.search(regex,text)
print(match.group(0))

text = '''malatesh@gmail.com
malatesh@@gmail.com
malatesh@4gmail.com
malatesh178@gmail.com
malatesh@yahoo.com
malatesh@outlook.com'''
regex = r"([a-zA-Z0-9_$\-]+)@([a-zA-Z]+.com)"
match = re.search(regex,text)
print(match.group(0))
print(match.group(1))
print(match.group(2))

text = '''malatesh@gmail.com
malatesh@@gmail.com
malatesh@4gmail.com
malatesh178@gmail.com
malatesh@yahoo.com
malatesh@outlook.com'''
regex = r"([a-zA-Z0-9_$\-]+)@([a-zA-Z]+.com)"
itr = re.finditer(regex,text)

for m in itr:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))

text = '''malatesh@gmail.com
malatesh@@gmail.com
malatesh@4gmail.com
malatesh178@gmail.com
malatesh@yahoo.com
malatesh@outlook.com'''
regex = r"@[a-zA-Z]+.com"
s = re.sub(regex,"@rooman.com",text)
print(s)

text = '''malatesh@gmail.com
malatesh@@gmail.com
malatesh@4gmail.com
malatesh178@gmail.com
malatesh@yahoo.com
malatesh@outlook.com'''
regex = r"@[a-zA-Z]+.com"
s = re.subn(regex,"@rooman.com",text)
print(s)

text = "2004/10/08"
print(re.split(r"[/|-]",text))
