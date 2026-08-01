# 41. Write a program to count the frequency of elements in a list using a dictionary.
numbers = list(map(int, input("Enter numbers: ").split()))
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Frequency of Elements:")
for key, value in frequency.items():
    print(key, "=", value)

# 42. Write a program to merge two dictionaries.
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}
merged = dict1.copy()
merged.update(dict2)
print("\nMerged Dictionary =", merged)

# 43. Write a program to sort a dictionary by values.
dictionary = {"a": 30, "b": 10, "c": 20, "d": 40}
sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
print("\nSorted Dictionary =", sorted_dict)

# 44. Write a program to find common elements using sets.
set1 = set(map(int, input("\nEnter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))
common = set1.intersection(set2)
print("Common Elements =", common)

# 45. Write a program to remove duplicate values from a list using a set.
numbers = list(map(int, input("\nEnter numbers: ").split()))
result = list(set(numbers))
print("List after removing duplicates =", result)

# 46. Write a function to calculate the factorial of a number.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("\nEnter a number: "))
print("Factorial =", factorial(num))

# 47. Write a function to check whether a number is prime.
def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("\nEnter a number: "))
if prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

# 48. Write a function to find the maximum of three numbers.
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum =", maximum(a, b, c))

# 49. Write a recursive function to calculate the Fibonacci series.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("\nEnter number of terms: "))
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")

# 50. Write a recursive function to reverse a string.
def reverse_string(string):
    if len(string) == 0:
        return string
    return reverse_string(string[1:]) + string[0]
string = input("\n\nEnter a string: ")
print("Reversed String =", reverse_string(string))