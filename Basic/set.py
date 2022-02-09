test_set1 = {'Python', '-', 'izm', '.', 'com'}
print(test_set1)

print('---------------------')

for i in test_set1:
    print(i)

# 辞書とsetの違い
test_dict = {}
test_set = {'Python'}
empty_set = set()

# 重複した値を持つことができない
test_set1 = {'Python', 'izm', '.', 'com', 'Python', '-', 'izm', '.', 'com'}
print(test_set1)

for i in test_set1:
    print(i)

# 要素の追加
test_set1 = set()
test_set1.add('Python')
test_set1.update({'-', 'izm', '.', 'com'})

print(test_set1)

# 要素の削除
test_set1 = {'python', '-', 'izm', '.', 'com'}

test_set1.remove('-')
test_set1.discard('.')

print(test_set1)

# frozenset
test_set1 = frozenset({'python', '-', 'izm', '.', 'com'})

# AttributeError
# test_set1.remove('-')
# test_set1.discard('.')

print(test_set1)
