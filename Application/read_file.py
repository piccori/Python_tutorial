# ファイルの読み込み
f = open('read.txt', 'r')

for row in f:
    print(row)

f.close()

# ファイルの書き込み
f = open('read.txt', 'w', encoding='utf-8')

f.write('Pythonでファイルに書き込みました！')

f.close()
