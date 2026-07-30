# 21. Write a program to reverse a string.

string = input("Enter a string: ")

reverse = string[::-1]

print("Reversed String =", reverse)


# 22. Write a program to check whether a string is a palindrome.

string = input("\nEnter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 23. Write a program to count vowels and consonants in a string.

string = input("\nEnter a string: ")

vowels = 0
consonants = 0

for ch in string.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)


# 24. Write a program to count the frequency of each character in a string.

string = input("\nEnter a string: ")

frequency = {}

for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:")
for key, value in frequency.items():
    print(key, "=", value)


# 25. Write a program to remove duplicate characters from a string.

string = input("\nEnter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result += ch

print("After Removing Duplicates =", result)


# 26. Write a program to find the longest word in a sentence.

sentence = input("\nEnter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word =", longest)


# 27. Write a program to replace spaces with hyphens.

string = input("\nEnter a string: ")

result = string.replace(" ", "-")

print("Result =", result)


# 28. Write a program to check whether two strings are anagrams.

string1 = input("\nEnter first string: ")
string2 = input("Enter second string: ")

if sorted(string1.lower()) == sorted(string2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")


# 29. Write a program to count the occurrence of a substring.

string = input("\nEnter a string: ")
substring = input("Enter substring: ")

count = string.count(substring)

print("Occurrence =", count)


# 30. Write a program to convert the first letter of every word to uppercase.

string = input("\nEnter a sentence: ")

result = string.title()

print("Result =", result)