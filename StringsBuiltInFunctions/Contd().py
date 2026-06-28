# without using built in function
url = ["https://www. google.com/", "https: //www.youtube.com/",
"http://www.xyz.com","http://www.abc.org"]
for i in url:
    if i[0:5:1] == "https":
        print(i)


# with built in function find starting with https
url = ["https://www. google.com/", "https: //www.youtube.com/",
"http://www.xyz.com","http://www.abc.org"]
for i in url:
    if i.startswith("https"):
        print(i)


# with built in function find start with http
url = ["https://www. google.com/", "https: //www.youtube.com/",
"http://www.xyz.com","http://www.abc.org"]
for i in url:
    if i.startswith("http"):
        print(i)


# with built in function find ends with com
url = ["https://www. google.com/", "https: //www.youtube.com/",
"http://www.xyz.com","http://www.abc.org"]
for i in url:
    if i.endswith("com"):
        print(i)


# without built in function find the string ends with "com" or "com/"
url = ["https://www. google.com/", "https: //www.youtube.com/",
"http://www.xyz.com","http://www.abc.org "]
for i in url:
    if i[len(i)-3::] == "com" or i[len(i)-4::] == "com/":
        print(i)


# with built in function find the string ends with "com" or "com/"
url = ["https://www. google.com/", "https: //www.youtube.com/",
"http://www.xyz.com","http://www.abc.org "]
for i in url:
    if i.endswith("com") or i.endswith("com/"):
        print(i)


# without built in function find the string ends with "com" or "com/"
url = ["https://www. google.com/", "https: //www.youtube.com/",
"http://www.xyz.com","http://www.abc.org "]
for i in url:
    if i.endswith(("com","com/")):
        print(i)


# program to count count number of upper case, lower case, number of special charecters present in a string.
s = input("enter a string\n")
low_count,up_count,sp_count,num_count = 0,0,0,0

for i in s:
    if ord(i)>=97 and ord(i)<=122:
        low_count = low_count+1
    elif ord(i)>=65 and ord(i)<=90:
        up_count = up_count+1
    elif ord(i)>=58 and ord(i)<=64:
        sp_count = sp_count+1
    elif ord(i)>=1 and ord(i)<=31:
        num_count = num_count+1
    else:
        print("")
print(f"lower case:{low_count},upper case:{up_count},speacial character:{sp_count},number:{num_count}")


s = input("Enter a string: ")
low_count = 0
up_count = 0
sp_count = 0
num_count = 0
for i in s:
    if i.islower():
        low_count += 1
    elif i.isupper():
        up_count += 1
    elif i.isnumeric():
        num_count += 1
    else:
        sp_count += 1
print("Lowercase:", low_count)
print("Uppercase:", up_count)
print("Special Characters:", sp_count)
print("Numbers:", num_count)



