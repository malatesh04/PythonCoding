text = input("enter the string \n").strip()
print("User entered text -->",text)
rev_text = text[::-1]
print("Reversed text -->",rev_text)

if text == rev_text:
    print(text,"the text is palindrome")
else:
    print(text,"the text is not palindrome")

