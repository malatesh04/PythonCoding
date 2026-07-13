# FIND THE SUM OF MINIMUM NUMBER AND THE MAXIMUM NUMBER OF A LIST WITHOUT USING IN-BUILT FUNCTIONS
# lst = [50,80,40,20,10,30]
lst = eval(input("enter the list between []\n"))
min = lst[0]
max = lst[0]

for i in range(1,len(lst)):
    if lst[i]<min:
        min = lst[i]
    elif lst[i]>max:
        max = lst[i]
print("max + min =",max+min)

# find lenth of the list without using built in function
lst = [10,20,30,40,50,60]
count = 0
for i in lst:
    count += 1
print(count)

# finding total sum of the list
lst = [10,20,30]
sum = 0
for i in lst:
    sum += i
print(sum)

# finding total product of the list
lst = [10,20,30]
product = 1
for i in lst:
    sum *= i
print(product)