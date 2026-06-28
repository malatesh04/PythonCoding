c = "a"
print(chr(ord(c)-32))
b = "A"
print(ord(b))

# converting small letter into capital letter
s = input("enter strring\n")
s_upper = "" 

for i in s:
    if ord(i) >= 97 and ord(i) <= 122:
        s_upper += chr(ord(i)-32);
    else: 
        s_upper += i;
print(s)
print(s_upper)

# using built in function
s = input("enter a string \n")
s_upper = s.upper()
print(s)
print(s_upper)

# converting upper to lower
s = input("enter a string \n")
s_lower = ""

for i in s:
    if ord(i)>=65 and ord(i)<=97 :
        s_lower = s_lower + chr(ord(i)+32)
    else:
        s_lower = s_lower + i
print(s)
print(s_lower)

# using built in function
s = input("enter a string\n")
s_lower = s.lower()
print(s)
print(s_lower)