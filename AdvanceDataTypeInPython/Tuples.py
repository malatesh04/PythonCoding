# Tuple dataTyppe: -->()
# --> this is also heterogius and homogenius in nature
# --> immutable in nature 

t = (10, 99.9, "python", True)
print(t)
print(type(t))

# ondu specific element naa horaga takkobek andra hing hakbek
print(t[0]) #edu positive indexing 
print(t[-4]) #edu negative indexing
# the sequence having both positive and negative indexing which 
# ever want you take from its indexing value

# append --> append support agalla adakke error barutta
t.append(27)
print(t)

# Remove --> remove support agalla adakke error barutt
t.remove(True)
print(t)