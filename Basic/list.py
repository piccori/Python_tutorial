test_list1 = ['python', '-', 'izm', '.', 'com']

print(test_list1)

print('-----------------------')

for i in test_list1:
    print(i)

# 要素の追加
test_list1 = []
print(test_list1)

test_list1.append('Python')
test_list1.append('-')
test_list1.append('izm')
test_list1.append('com')

print(test_list1)

# インデックスを指定して追加
test_list1 = ['Python', 'izm', 'com']
print(test_list1)

print('-----------------------')

test_list1.insert(1, '-')
test_list1.insert(3, '.')

print(test_list1)

test_list1.insert(0, 'http://www.')

print(test_list1)

# 要素の削除１
test_list1 = ['1', '2', '3', '2', '1']
print(test_list1)

print('-----------------------')
test_list1.remove('2')

print(test_list1)

# 要素の削除2
test_list1 = ['1', '2', '3', '2', '1']
print(test_list1)

print('-----------------------')
print(test_list1.pop(1))
print(test_list1)

print(test_list1.pop())
print(test_list1)

# 要素のインデックスを取得
test_list1 = ['100', '200', '300', '200', '100']

print(test_list1.index('200'))

# リスト内での要素数を取得
test_list1 = ['100', '200', '300', '200', '100']

print(test_list1.count('200'))
