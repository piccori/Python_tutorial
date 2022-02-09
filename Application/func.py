def test_func():
    print('call test_func')


def test(num1, num2, oprn=1):

    if oprn == 1:
        print('足し算開始')
        print(num1 + num2)

    elif oprn == 2:
        print('引き算開始')
        print(num1 - num2)

    elif oprn == 3:
        print('掛け算開始')
        print(num1 * num2)

    elif oprn == 4:
        print('割り算開始')
        print(num1 / num2)

    else:
        print('不明なオペレーション指定です')


test_func()
test(100, 10, 3)
