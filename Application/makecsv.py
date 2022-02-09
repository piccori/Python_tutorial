import csv


# csv_file = open('./python.csv', 'w', newline='')
# writer = csv.writer(csv_file)


csv_file = open('./python.csv', 'w', newline='')

# いろいろ変更
# writer = csv.writer(
#     csv_file,
#     quoting=csv.QUOTE_ALL,
#     delimiter=':',
#     quotechar='`'
# )

# タブ文字
writer = csv.writer(
    csv_file,
    dialect=csv.excel_tab,
)

# 一行の書き込み
row = ('python', '-', 'izm', '1')
writer.writerow(row)
# 複数行の書き込み
rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()


# csvファイルの読み込み
csv_file = open('./python.csv', 'r', newline='')
reader = csv.reader(csv_file)

for row in reader:
    print('-------')
    for cell in row:
        print(cell)

csv_file.close()
