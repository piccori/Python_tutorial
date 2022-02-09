test_dict1 = {'YEAR': '2022', 'MONTH': '1', 'DAY': '1'}

print(test_dict1)

print('=========================')

for i in test_dict1:

    print(i)
    print(test_dict1)
    print('------------------------')

print(test_dict1['YEAR'])
print('------------------------')

print(test_dict1.get('YEAR'))
print(test_dict1.get('YEARS'))

print('------------------------')

print(test_dict1.get('YEAR', 'NOT FOUND'))
print(test_dict1.get('YEARS', 'NOT FOUND'))


# 要素の追加
test_dict1 = {}

print(test_dict1)

print('=========================')

test_dict1['YEAR'] = '2020'
test_dict1['MONTH'] = '2'
test_dict1['DAY'] = '20'

print(test_dict1)

# 要素の削除
test_dict1 = {'YEAR': '2022', 'MONTH': '1', 'DAY': '1'}

print(test_dict1)

print('=========================')

del test_dict1['DAY']
print(test_dict1)

# keyやvalueだけを取得する
test_dict1 = {'YEAR': '2022', 'MONTH': '1', 'DAY': '1'}

print(test_dict1)

print('=========================')

print(test_dict1.keys())
print(test_dict1.values())

# keyとvaluesを同時に取得
test_dict1 = {'YEAR': '2022', 'MONTH': '1', 'DAY': '1'}

print(test_dict1)
print('=========================')

for k, v in test_dict1.items():
    print(k, v)

# keyを保持しているのを確認
test_dict1 = {'YEAR': '2020', 'MONTH': '1', 'DAY': '20'}
print(test_dict1)

print('=========================')
print('YEAR' in test_dict1)
print('YEARS' in test_dict1)
