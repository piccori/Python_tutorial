print('Python-izm')
print("Python-izm")

test_str = """
test_1
test_2
"""
print(test_str)

# 文字列の連結
test_str = 'Python'
test_str = test_str + '-'
test_str = test_str + 'izm'

print(test_str)

test_str = '012'
test_str += '345'
test_str += '678'
test_str += '9'

print(test_str)

test_str = '012' * 3

print(test_str)

# 文字列へ変換
test_integer = 100

print(str(test_integer) + '円')

# 文字列の置換
test_str = 'Python-izm'

print(test_str.replace('izm', 'ism'))

# 文字列の分割
test_str = 'python-izm'

print(test_str.split('-'))

# 文字列の行揃え
test_str = '1234'

print(test_str.rjust(10, '0'))
print(test_str.rjust(10, '!'))

test_str = '1234'
# 0で埋め合わせする
print(test_str.zfill(10))
print(test_str.zfill(5))

# 文字列の検索
test_str = 'python-izm'
# 文字列の先頭が任意も文字なのか True/False
print(test_str.startswith('python'))
print(test_str.startswith('izm'))
# 文字列中に任意の文字が含まれているか
print('z' in test_str)
print('s' in test_str)

# 大文字・小文字の変換
test_str = 'Python-izm.Com'

print(test_str.upper())
print(test_str.lower())

# 先頭・末尾の削除
print('---------------------------')

test_str = '            python-izm'
print(test_str)
# 先頭から空白を削除
test_str = test_str.lstrip()
print(test_str)
#
test_str = test_str.lstrip('python')
print(test_str)

print('---------------------------')

test_str = 'python-izm          '
print(test_str + '/')
# 末尾から空白を削除
test_str = test_str.rstrip()
print(test_str + '/')

test_str = test_str.rstrip('com')
print(test_str)
