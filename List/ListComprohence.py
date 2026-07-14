# # if else in compreshension
# lst = [3,6,5,4,2]
# even_add = []
# odd_sq = []

# for i in lst:
#     if i%2 == 0:
#         even_add.append(i+i)
#     else:
#         odd_sq.append(i**2)
# print(even_add)
# print(odd_sq)

# lst = [3,6,5,4,2]
# even_add = [i+i for i in lst if i%2 == 0]
# odd_sq = [i**2 for i in lst else i%2 != 0]

lst = [3,6,5,4,2]
res = []

for i in lst:
    if i%2==0:
        res.append(i*i)
    else:
        res.append(i+i)
print(res)
