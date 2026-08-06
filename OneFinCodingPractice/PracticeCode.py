# 1. Read and Print a List
numbers = list(map(int, input("1. Enter numbers: ").split()))
print(numbers)

# 2. Find Length
numbers = list(map(int, input("\n2. Enter numbers: ").split()))
print("Length:", len(numbers))

# 3. Find Maximum
numbers = list(map(int, input("\n3. Enter numbers: ").split()))
print("Maximum:", max(numbers))

# 4. Find Minimum
numbers = list(map(int, input("\n4. Enter numbers: ").split()))
print("Minimum:", min(numbers))

# 5. Find Sum
numbers = list(map(int, input("\n5. Enter numbers: ").split()))
print("Sum:", sum(numbers))

# 6. Find Average
numbers = list(map(int, input("\n6. Enter numbers: ").split()))
print("Average:", sum(numbers) / len(numbers))

# 7. Find Largest Without max()
numbers = list(map(int, input("\n7. Enter numbers: ").split()))
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest:", largest)

# 8. Find Smallest Without min()
numbers = list(map(int, input("\n8. Enter numbers: ").split()))
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest:", smallest)

# 9. Reverse List
numbers = list(map(int, input("\n9. Enter numbers: ").split()))
print("Reversed:", numbers[::-1])

# 10. Sort List
numbers = list(map(int, input("\n10. Enter numbers: ").split()))
numbers.sort()
print("Sorted:", numbers)

# 11. Count Even and Odd
numbers = list(map(int, input("\n11. Enter numbers: ").split()))
even = odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)

# 12. Find Second Largest
numbers = list(map(int, input("\n12. Enter numbers: ").split()))
numbers.sort()
print("Second Largest:", numbers[-2])

# 13. Remove Duplicates
numbers = list(map(int, input("\n13. Enter numbers: ").split()))
numbers = list(set(numbers))
print("Without Duplicates:", numbers)

# 14. Search an Element
numbers = list(map(int, input("\n14. Enter numbers: ").split()))
item = int(input("Enter element to search: "))
if item in numbers:
    print("Found")
else:
    print("Not Found")

# 15. Count Occurrences
numbers = list(map(int, input("\n15. Enter numbers: ").split()))
item = int(input("Enter element: "))
print("Count:", numbers.count(item))

# 16. Merge Two Lists
list1 = list(map(int, input("\n16. Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
print("Merged List:", list1 + list2)

# 17. Find Common Elements
list1 = list(map(int, input("\n17. Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
common = []
for num in list1:
    if num in list2:
        common.append(num)
print("Common Elements:", common)

# 18. Square Each Element
numbers = list(map(int, input("\n18. Enter numbers: ").split()))
result = []
for num in numbers:
    result.append(num * num)
print("Squares:", result)

# 19. Count Positive and Negative Numbers
numbers = list(map(int, input("\n19. Enter numbers: ").split()))
positive = negative = 0
for num in numbers:
    if num >= 0:
        positive += 1
    else:
        negative += 1
print("Positive:", positive)
print("Negative:", negative)

# 20. Find Largest and Smallest Together
numbers = list(map(int, input("\n20. Enter numbers: ").split()))
largest = smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)