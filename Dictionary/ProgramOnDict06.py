# # jack and jill went up the hill --> give which len is higher top to bottom with alphabetic order

# lst = input().lower().split()
# d = {}

# for i in lst:
#     if len(i) not in d:
#         d[len(i)] = []
#         d[len(i)].append(i)
#     else:
#         d[len(i)].append(i)
# s_d = sorted(d.keys(), reverse=True)

# for i in s_d:
#     for j in sorted(d[i]):
#         print(j)
        

# # Dictinary comprohension -->

# # 2nd programm
# # without comprohension
# lst = input().split()
# d = {}
# for i in lst:
#     d[i] = len(i)
# print(d)

# # with comprohension
# print({i:len(i) for i in input().split()})


# # program 3:
# # without comprohension
# lst = [1,2,3,4,5,6,7,8,9]
# d = {}
# for i in lst:
#     if i%2 == 0:
#         d[i] = i**2
# print(d)

# # with comprohension
# print({i:i**2 for i in [1,2,3,4,5,6,7,8,9] if i%2==0})

# # without comprohension
# lst = [1,2,3,4,5,6,7,8,9]
# d = {}
# for i in lst:
#     if i%2 == 0:
#         d[i] = i**2
#     else:
#         d[i] = i**3
# print(d)

# # with comprohension
# print({i:i**2 if i%2 == 0 else i**3 for i in [1,2,3,4,5,6,7,8,9]})


# # program 4:
# # without comprohension
# lst = ['india','srilanka','usa','poland']
# d = {}
# for i in lst:
#     if len(i) < 6:
#         if len(i) % 2 == 0:
#             d[i.upper()] = len(i)**2
#         else:
#             d[i.upper()] = len(i)**3
#     else:
#         if len(i) % 2 == 0:
#             d[i.lower()] = len(i)**2
#         else:
#             d[i.lower()] = len(i)**3
# print(d)

# # with comprohension
print({(i.upper() if len(i) < 6 else i.lower()):(len(i)**2 if len(i) % 2 == 0 else len(i)**3)for i in ['india','srilanka','usa','poland']})