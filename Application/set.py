test_set1 = ({'python', '-', 'izm', '.', 'com'})

print(test_set1.isdisjoint({'python', 'izm'}))
print(test_set1.isdisjoint({1, 2, 3}))

print('---------------')

print(test_set1.issubset({'python', 'izm'}))
print(test_set1.issubset({'www', 'python', '-', 'izm', '.', 'com'}))

print('---------------')

print(test_set1.issubset({'python', 'izm'}))
print(test_set1.issubset({'www', 'python', '-', 'izm', '.', 'com'}))
# issubsetは全要素が引数の反復可能オブジェクトに含まれているときにTrue
# issupersetは引数の反復可能オブジェクトの全要素がセットに含まれているときにTrue

test_set_1 = {'python', '-', 'izm', '.', 'com'}

# issubsetと同じ
print(test_set_1 <= {'python', 'izm'})
print(test_set_1 <= {'www', 'python', '-', 'izm', '.', 'com'})

print('----------------------------')

# issupersetと同じ
print(test_set_1 >= {'python', 'izm'})
print(test_set_1 >= {'www', 'python', '-', 'izm', '.', 'com'})

# セットを比較して作成
test_set1 = {'python', 'izm', 'com'}

print(test_set1.union({'python', 'www'}))
print(test_set1.intersection({'python', 'www'}))
print(test_set1.difference({'python', 'www'}))
print(test_set1.symmetric_difference({'python', 'www'}))

# 演算子でも同じ結果
test_set_1 = {'python', 'izm', 'com'}

print(test_set_1 | {'python', 'www'})
print(test_set_1 & {'python', 'www'})
print(test_set_1 - {'python', 'www'})
print(test_set_1 ^ {'python', 'www'})

# セットを比較して更新
test_set1 = {'python', 'izm', 'com'}
test_set1.intersection_update({'python', 'www'})
print(test_set1)

test_set1 = {'python', 'izm', 'com'}
test_set1.difference_update({'python', 'www'})
print(test_set1)

test_set1 = {'python', 'izm', 'com'}
test_set1.symmetric_difference_update({'python', 'www'})
print(test_set1)

# 演算子でも同じ結果
test_set_1 = {'python', 'izm', 'com'}
test_set_1 &= {'python', 'www'}
print(test_set_1)

test_set_1 = {'python', 'izm', 'com'}
test_set_1 -= {'python', 'www'}
print(test_set_1)

test_set_1 = {'python', 'izm', 'com'}
test_set_1 ^= {'python', 'www'}
print(test_set_1)
