# slice --> string_name[start(inclusive):stop(exclusive):step]

s = "MALATESH BASAVANNEPPA NEGALUR"
print(s)
print(s[0])
print(s[::])  # --> default when you dont give anything then [start index : stop index+1 : 1]
print(s[0:8:1]) # MALATESH printing
print(s[29:21:-1]) #reverse substring printing
print(s[-1:-8:-1]) #reverse using minus indexing
print(s[::-1])