import re

text = "7676115923 76761123"
regex = r"\d{10}"
print(re.search(regex,text))

# or

text = "7676115923 76761123 9686520989"
p= re.compile(r"\d{10}")
print(p.findall(text))

text = ['7676115923',
'9686520989',
'9448344099',
'8197344099',
'914808162',
'89288188639']
p = re.compile(r"\b\d{5}[02468]\d{4}\b")

for i in text:
    if p.search(i) != None:
        print(i,"valid")
    else:
        print(i,"not valid")
