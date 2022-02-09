with open('file.txt', 'r+') as f:
    f.write('Hello World')
    f.seek(0)
    print(f.read(1))
    print(f.read(1))
    print(f.read(1))
    print(f.read(1))
    print(f.read(1))
    f.seek(6)
    print(f.read(1))
# 自動的にcloseされる
