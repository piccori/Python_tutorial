import csv


csv_file = open('./python.csv', 'w', newline='')
writer = csv.writer(csv_file)

row = ('Python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('Python', '-', 'izm', '2'))
rows.append(('Python', '-', 'izm', '3'))
rows.append(('P,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()
