# # PROGRAM TO CHECK IF THE EXPRESSION CONTAINS BALANCED PARENTHESES 

# s = input("enter an expression with brackets\n")
# lst = []

# for i in s:
#     if i=='[' or i=='(' or i==')':
#         lst.append(i)
#     elif i==']' and lst[-1]=='[':
#         lst.pop()
#     elif i==')' and lst[-1]=='(':
#         lst.pop()
#     elif i=='{' and lst[-1]=='}':
#         lst.pop()
#     else:
#         break

# if len(lst) == 0:
#     print(s,"expression is balanced")
# else:
#     print(s,"expression is not balanced")

# # COMPARISON OF LISTS
# lst1 = [7,5,3]
# lst2 = [7,5,3]
# print(lst1 == lst2)

# lst1 = [7,5,3]
# lst2 = [7,15,3]
# print(lst1 == lst2)

# lst1 = [7,5,3]
# lst2 = [7,5,3]
# print(lst1 != lst2)

# lst1 = [7,5,3]
# lst2 = [7,15,3]
# print(lst1 != lst2)

# lst1 = [7,5,3]
# lst2 = [10,5,3]
# print(lst1 > lst2)

lst1 = [7,5,3]
lst2 = [7,5,1]
print(lst1 > lst2)