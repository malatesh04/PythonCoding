# 11. Write a program to check whether a number is prime.
num = int(input("Enter a number: "))
if num < 2:
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

# 12. Write a program to print all prime numbers between 1 and N.
n = int(input("Enter N: "))
print("Prime Numbers:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# 13. Write a program to find the sum of digits of a number.
num = int(input("\n\nEnter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("Sum of Digits =", sum)

# 14. Write a program to count the number of digits in a number.
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count = count + 1
    num = num // 10
print("Number of Digits =", count)

# 15. Write a program to print multiplication tables from 1 to 10.
for i in range(1, 11):
    print("\nTable of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

# 16. Write a program to find the GCD and LCM of two numbers.
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
small = min(a, b)
gcd = 1
for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
lcm = (a * b) // gcd
print("GCD =", gcd)
print("LCM =", lcm)

# 17. Write a program to check whether a number is an Armstrong number.
num = int(input("\nEnter a number: "))
original = num
digits = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + (digit ** digits)
    num = num // 10
if original == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# 18. Write a program to print all Armstrong numbers between 1 and N.
n = int(input("\nEnter N: "))
print("Armstrong Numbers:")
for num in range(1, n + 1):
    original = num
    digits = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** digits)
        temp = temp // 10
    if original == sum:
        print(original, end=" ")

# 19. Write a program to calculate the power of a number without using **.
base = int(input("\n\nEnter base: "))
power = int(input("Enter power: "))
result = 1
for i in range(power):
    result = result * base
print("Answer =", result)

# 20. Write a program to print patterns using stars (*).
rows = int(input("\nEnter number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()