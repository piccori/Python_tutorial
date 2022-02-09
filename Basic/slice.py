test_list = ['https', 'www', 'python', 'izm', 'com']
# 全ての要素の取得
print(test_list[:])
print(test_list[::])

# 要素の取得
print(test_list[:4])
print(test_list[2:])

print(test_list[::2])
print(test_list[3:5])

print(test_list[-1:])
print(test_list[:-1])
print(test_list[::-1])

# 要素の代入
test_list[1:3] = ('WWW', 'PYTHON')
print(test_list)
