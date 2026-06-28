# swapping two numbers

a = int(input("enter a value -->"))
b = int(input("enter b value -->"))

temp = a
a = b
b = temp

print("After swapping")
print(a,"is a value")
print(b,"is b value")



# Finding  even odd sum number 

even_sum, odd_sum = 0, 0
n = int(input("enter a value of n\n"))

for i in range(1,n+1):
    if i%2==0:
        even_sum += i
        continue
    odd_sum +=i
print("even sum is: ",even_sum)
print("odd sum is: ",odd_sum)