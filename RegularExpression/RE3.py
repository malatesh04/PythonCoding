import re
text = '''abcpqrxyz
pqrxyzabc
pqrabcxyz
abc'''
regex = r"abc"
l = re.findall(regex,text)
print(l)

# BOUNDARY CONCEPT
text = '''abcpqrxyz
pqrxyzabc
pqrabcxyz
abc'''
regex = r"\babc"
l = re.findall(regex,text)
print(l)

text = '''abcpqrxyz
pqrxyzabc
pqrabcxyz
abc'''
regex = r"\babc\b"
l = re.findall(regex,text)
print(l)

text = '''abcpqrxyz
pqrxyzabc
pqrabcxyz
abc'''
regex = r"\Babc\B"
l = re.findall(regex,text)
print(l)

text = '''abcpqrxyz
pqrxyzabc
pqrabcxyz
abc'''
regex = r"\Babc\B" #not boundary
match = re.search(regex,text)
print(match)

text = "python is the best"
regex = r"^[a-zA-Z]+"
l = re.findall(regex,text)
print(l)
match = re.match(regex,text)
print(match)

text = "python is the best"
regex = r"[a-zA-Z]+$"
match = re.search(regex,text)
print(match)
print(match.group)

text = "python is best prgramming language this"
regex = r"\b[a-zA-Z]{4}\b" #finding such word ehich has 4 character
l = re.findall(regex,text)
print(l)

text = '''malatesh@gmail.com
malatesh@@gmail.com
malatesh@4gmail.com
malatesh178@gmail.com'''
regex = r"[a-zA-Z0-9_$\-]+@gmail.com"
l = re.findall(regex,text)
print(l)

text = '''malatesh@gmail.com
malatesh@@gmail.com
malatesh@4gmail.com
malatesh178@gmail.com
malatesh@yahoo.com
malatesh@outlook.com'''
regex = r"[a-zA-Z0-9_$\-]+@[a-zA-Z]+.com"
l = re.findall(regex,text)
print(l)