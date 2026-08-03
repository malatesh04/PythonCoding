# 71. Two Sum problem.
# 72. Find the first non-repeating character in a string.
# 73. Find the duplicate elements in a list.
# 74. Find the intersection of two arrays.
# 75. Check whether two lists are equal.
# 76. Find the longest common prefix among strings.
# 77. Move all zeros to the end of a list.
# 78. Find the missing number from an array of 1 to N.
# 79. Find the majority element in a list.
# 80. Implement binary search.

# 71. Two Sum problem.
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))
found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Indices:", i, j)
            found = True
            break
    if found:
        break
if not found:
    print("No pair found")

# 72. Find the first non-repeating character in a string.
string = input("\nEnter a string: ")
for ch in string:
    if string.count(ch) == 1:
        print("First Non-Repeating Character =", ch)
        break
else:
    print("No Non-Repeating Character")

# 73. Find the duplicate elements in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("Duplicate Elements =", duplicates)

# 74. Find the intersection of two arrays.
array1 = list(map(int, input("\nEnter first array: ").split()))
array2 = list(map(int, input("Enter second array: ").split()))
intersection = []
for num in array1:
    if num in array2 and num not in intersection:
        intersection.append(num)
print("Intersection =", intersection)

# 75. Check whether two lists are equal.
list1 = list(map(int, input("\nEnter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
if list1 == list2:
    print("Lists are Equal")
else:
    print("Lists are Not Equal")

# 76. Find the longest common prefix among strings.
strings = input("\nEnter strings separated by space: ").split()
prefix = strings[0]
for word in strings[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest Common Prefix =", prefix)

# 77. Move all zeros to the end of a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
result = []
count = 0
for num in numbers:
    if num != 0:
        result.append(num)
    else:
        count += 1
result.extend([0] * count)
print("Result =", result)

# 78. Find the missing number from an array of 1 to N.
numbers = list(map(int, input("\nEnter numbers: ").split()))
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
print("Missing Number =", expected_sum - actual_sum)

# 79. Find the majority element in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
majority = None
for num in numbers:
    if numbers.count(num) > len(numbers) // 2:
        majority = num
        break
if majority is not None:
    print("Majority Element =", majority)
else:
    print("No Majority Element")

# 80. Implement binary search.
numbers = list(map(int, input("\nEnter sorted numbers: ").split()))
target = int(input("Enter target: "))
low = 0
high = len(numbers) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Element Found at Index", mid)
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Element Not Found")

