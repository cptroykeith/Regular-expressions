import re 
x = 'My 2 favorite are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
#returns an empty set when there is no match
y = re.findall('[AEIOU]+',x)
print(y)