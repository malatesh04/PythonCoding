# WAP to make which or vowel make capital and number is erase

s = "Error 404 page not found"
table = s.maketrans("aeiou" ,"AEIOU" ,"123456789")
s_table = s.translate(table)
print(s)
print(s_table)
