# # WAP to find 3 substring character in given string 
# s = input("enter a string \n")
# for i in range(0,len(s)-2):
#     print(s[i:i+3]) 

# # WAP to find 4 substring character in given string
# s = input("enter a string \n") 
# for i in range(0,len(s)-3):
#     print(s[i:i+4])

# # program to give output without 1st and last string character
# s = input("enter a string \n")
# print(s[1:len(s)-1])

# # WAP to character of string in the reverse oreder except the 1st and last character
# s = input("enter a string \n")
# print(s[len(s)-2:0:-1])

# program to check whether the given string is palindrome
s = input("enter a string \n")
if s == s[::-1]:
    print(True)
    print(f"the given string {s} is palindrome")
else:
    print(False)
    print(f"the given string {s} is not palindrome")