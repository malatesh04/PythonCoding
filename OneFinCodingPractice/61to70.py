# 61. Write a program to create and write to a text file.

# 62. Write a program to read a text file.

# 63. Write a program to count words in a file.

# 64. Write a program to copy the contents of one file to another.

# 65. Write a program to handle ZeroDivisionError.

# 66. Write a program to handle FileNotFoundError.

# 67. Write a program using try, except, else, and finally.

# 68. Write a custom exception class.

# 69. Write a program to append data to a file.

# 70. Write a program to count lines, words, and characters in a file.


# 61. Write a program to create and write to a text file.
file = open("sample.txt", "w")
file.write("Hello, Welcome to Python File Handling.")
file.close()
print("Data written successfully.")

# 62. Write a program to read a text file.
file = open("sample.txt", "r")
data = file.read()
file.close()
print("\nFile Content:")
print(data)

# 63. Write a program to count words in a file.
file = open("sample.txt", "r")
data = file.read()
file.close()
words = data.split()
print("\nNumber of Words =", len(words))

# 64. Write a program to copy the contents of one file to another.
source = open("sample.txt", "r")
data = source.read()
source.close()
destination = open("copy.txt", "w")
destination.write(data)
destination.close()
print("\nFile copied successfully.")

# 65. Write a program to handle ZeroDivisionError.
try:
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 66. Write a program to handle FileNotFoundError.
try:
    file = open("demo.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found.")

# 67. Write a program using try, except, else, and finally.
try:
    num = int(input("\nEnter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result =", result)
finally:
    print("Program Finished.")

# 68. Write a custom exception class.
class NegativeNumberError(Exception):
    pass
try:
    num = int(input("\nEnter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    print("You entered:", num)
except NegativeNumberError as e:
    print(e)

# 69. Write a program to append data to a file.
file = open("sample.txt", "a")
file.write("\nThis is appended data.")
file.close()
print("\nData appended successfully.")

# 70. Write a program to count lines, words, and characters in a file.
file = open("sample.txt", "r")
data = file.read()
file.close()
lines = data.split("\n")
words = data.split()
print("\nLines =", len(lines))
print("Words =", len(words))
print("Characters =", len(data))
