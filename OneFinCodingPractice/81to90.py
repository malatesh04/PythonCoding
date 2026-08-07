# 81. Write a program to check whether a string contains only digits.
string = input("Enter a string: ")
if string.isdigit():
    print("String contains only digits.")
else:
    print("String does not contain only digits.")

# 82. Write a program to remove all spaces from a string.
string = input("\nEnter a string: ")
result = string.replace(" ", "")
print("Result =", result)

# 83. Write a program to find the smallest element in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest Element =", smallest)

# 84. Write a program to find the sum of all elements in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
total = 0
for num in numbers:
    total += num
print("Sum =", total)

# 85. Write a program to find the average of list elements.
numbers = list(map(int, input("\nEnter numbers: ").split()))
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average =", average)

# 86. Write a program to split a list into even and odd numbers.
numbers = list(map(int, input("\nEnter numbers: ").split()))
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even Numbers =", even)
print("Odd Numbers =", odd)

# 87. Write a program to find the maximum and minimum elements in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum =", maximum)
print("Minimum =", minimum)

# 88. Write a program to insert an element at a specific position in a list
numbers = list(map(int, input("\nEnter numbers: ").split()))
element = int(input("Enter element: "))
position = int(input("Enter position: "))
numbers.insert(position, element)
print("Updated List =", numbers)

# 89. Write a program to delete an element from a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
element = int(input("Enter element to delete: "))
if element in numbers:
    numbers.remove(element)
    print("Updated List =", numbers)
else:
    print("Element not found.")

# 90. Write a program to count the occurrence of an element in a list.
numbers = list(map(int, input("\nEnter numbers: ").split()))
element = int(input("Enter element: "))
count = numbers.count(element)
print("Occurrence =", count)