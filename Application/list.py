from itertools import zip_longest


python_list = []

python_list.append(100)
python_list.append(200)
python_list.append(10)
python_list.append(800)
python_list.append(60)

print('-----------------')
print('そのまま表示')
for val in python_list:
    print(val)

print('-----------------')
print('ソート表示')
for val in sorted(python_list):
    print(val)


python_list.sort()
print('-----------------')
print('ソート表示')
for val in python_list:
    print(val)


python_list = []
python_list.append('Python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')

print('-----------------')
print('そのまま表示')
for val in python_list:
    print(val)

print('-----------------')
print('逆順表示')
for val in reversed(python_list):
    print(val)

print('-----------------')
print('逆順表示')
for val in python_list[::-1]:
    print(val)

python_list.reverse()
print('-----------------')
print('逆順表示')
for val in python_list:
    print(val)


# インデックス付きループ
for i, k in enumerate(python_list):
    print(i, k)

# 連結
elem = ['www', 'python-izm', 'com']

name = ''
for val in elem:
    name += val + '.'
print(name)

print('.'.join(elem))

item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55, 0]

for item_name, stock_count in zip(item_list, stock_list):
    print(f'{item_name} / {stock_count}')


item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55]

for item_name, stock_count in zip_longest(item_list,
                                          stock_list,
                                          fillvalue='No Stock'):
    print(f'{item_name} / {stock_count}')


# 真偽判定
test_list1 = [0, 100, 300, 800, 150, 0, 40]
test_list2 = ([], [], [])
test_list3 = (['python', 'izm', 'com'], ['www'], ['http'])

print(all(test_list1))
print(all(test_list2))
print(all(test_list3))

# all関数でやっていること
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

print(any(test_list1))
print(any(test_list2))
print(any(test_list3))

# any関数でやっていること
# def any(iterable):
#     for element in iterable:
#         if element in iterable:
#             return True
#     return False
