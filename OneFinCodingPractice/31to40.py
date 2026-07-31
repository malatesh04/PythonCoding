# 31. Write a program to find the largest element in a list.
numbers = list(map(int, input("Enter numbers: ").split()))
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest Element =", largest)
# 32. Write a program to find the second largest element in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
numbers = list(set(numbers))
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print("Second Largest Element =", second_largest)

# 33. Write a program to remove duplicates from a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print("List after removing duplicates =", result)

# 34. Write a program to sort a list without using sort().
numbers = list(map(int, input("\nEnter numbers: ").split()))
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Sorted List =", numbers)

# 35. Write a program to merge two sorted lists.

list1 = list(map(int, input("\nEnter first sorted list: ").split()))
list2 = list(map(int, input("Enter second sorted list: ").split()))
merged = list1 + list2
for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]
print("Merged Sorted List =", merged)

# 36. Write a program to find common elements in two lists.
list1 = list(map(int, input("\nEnter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
common = []
for num in list1:
    if num in list2 and num not in common:
        common.append(num)
print("Common Elements =", common)

# 37. Write a program to rotate a list by K positions.
numbers = list(map(int, input("\nEnter numbers: ").split()))
k = int(input("Enter K: "))
k = k % len(numbers)
rotated = numbers[-k:] + numbers[:-k]
print("Rotated List =", rotated)

# 38. Write a program to count even and odd numbers in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Numbers =", even)
print("Odd Numbers =", odd)

# 39. Write a program to find the missing number in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing = expected_sum - actual_sum
print("Missing Number =", missing)

# 40. Write a program to reverse a list without using reverse().
numbers = list(map(int, input("\nEnter numbers: ").split()))
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])
print("Reversed List =", reversed_list)