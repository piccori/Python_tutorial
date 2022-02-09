for_sample = []
for_sample.append('pyhton')
for_sample.append('-')
for_sample.append('izm')
for_sample.append('for')
for_sample.append('statement')
for_sample.append('sample')

for value in for_sample:
    print(value)

test_list_1 = [['http', 'www'], ['python-izm', 'com']]

for value in test_list_1:
    print(value)

for value_1, value_2 in test_list_1:
    print(value_1, value_2)

for value in 'ABCDEFG':
    print(value)

for num in range(100):
    print(num)

    if num == 10:
        break

for num in range(100):
    if num % 10:
        continue

    print(num)
