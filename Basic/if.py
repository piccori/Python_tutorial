value = 2

if value == 1:
    print('valueの値は1です。')
elif value == 2:
    print('valueの値は2です。')
elif value == 3:
    print('valueの値は3です。')
else:
    print('該当する値はありません')


def value(value_1, value_2):
    if value_1 == 'Python':
        pass
    elif value_1 == 'python' and value_2 == 'izm':
        print('2番目の条件式がTrue')
    elif value_1 == 'PYTHON' or value_2 == 'IZM':
        print('3番目の条件式がTrue')


value('PYTHON', 'IZM')
