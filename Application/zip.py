import zipfile


# 複数のファイルをまとめるだけ
zipFile = zipfile.ZipFile('./compress_1.zip', 'w', zipfile.ZIP_STORED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()
# 複数のファイルをまとめ,ファイルサイズも圧縮
zipFile = zipfile.ZipFile('./compress_2.zip', 'w', zipfile.ZIP_DEFLATED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()
