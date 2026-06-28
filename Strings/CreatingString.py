# string we can represntede using single quote(''), multiquote(""), or triplequote('''''')

# string contain nothing
s1 = ''
print(s1)

# string contain one character
s2 = 'p'
print(s2)

# string contain set of character
s3 = 'python'
print(s3)

# converting float into string
s4 = str(99.99)
print(s4)
print(type(s4))

# string contain multiline words
s5 = '''c programm
python programm
java programm'''
print(s5)

string = "practice make man '''perfect'''"
string1 = "practice make man \"perfect\""
print(string)
print(string1)

s = "python"
print(s)
print(s[0])
for i in s:
    print(i)


n = int(input("enter the number --> \n"))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


s1 = "hello"
s2 = "world"
print(s1)
print(id(s1))
print(s2)
print(id(s2))
print(s1[4]) # s1 dinda "o" character print
print(id(s1[4])) # s1 "o" character address
print(s2[1]) # s2 dinda "o" character print
print(id(s2[1])) # s2 "o" character address same 

s1 = "p"
s2 = "p"
print(id(s1))
print(id(s2))


# string interning 
s1 = "hello"
s2 = "world"
print(s1, s2)
print(id(s1), id(s2))
print(id(s1[0]),id(s1[1]),id(s1[2]),id(s1[3]),id(s1[4]))
print(id(s2[0]),id(s2[1]),id(s2[2]),id(s2[3]),id(s2[4]))

