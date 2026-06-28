# using concatination 
lst = ["python","java","django","spring"]
s = ""
for i in lst:
    s = s + i
print(id(s))


# using join() built in function
lst = ["python","java","django","spring"]
s = "".join(lst)
print(s)