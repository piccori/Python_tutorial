import re


sentence = 'aaa abc aac abb abab 123 112 111'

pattern = 'ab.'
result = re.findall(pattern, sentence)
print(result)

pattern = 'a.b'
result = re.findall(pattern, sentence)
print(result)

pattern = 'a..'
result = re.findall(pattern, sentence)
print(result)

pattern = 'ab|aa'
result = re.findall(pattern, sentence)
print(result)

pattern = 'a{3}'
result = re.findall(pattern, sentence)
print(result)

pattern = '\d'
result = re.findall(pattern, sentence)
print(result)

pattern = '\d2'
result = re.findall(pattern, sentence)
print(result)

pattern = '\d\d'
result = re.findall(pattern, sentence)
print(result)
