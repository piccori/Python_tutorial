import os
import os.path


print(os.sep)
print(os.pathsep)
print(os.extsep)

# ファイルの拡張子の取得
print(os.path.splitext('splitext.py'))
print(os.path.splitext('C:/python/splitext.txt'))
print(os.path.splitext('splitext'))

# 改行コードの取得
test_str = 'python-izm.com'

print(test_str.replace('.', os.linesep))

# 環境変数の取得
for env in os.environ:
    print(env)

print('-----------------')
print(os.environ.get('windir'))
