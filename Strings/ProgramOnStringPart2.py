# Programm to reverse the second half of a string

s = input("enter a string \n")
print(s[:len(s)//2:] + s[len(s)-1:len(s)//2-1:-1])