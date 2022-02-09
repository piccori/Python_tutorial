def test_func(*args):
    print(args)


test_func(1, 2, 3, 4, 5)


def exsample_func(code, name, kana, *args, **kwargs):
    print(code, name, kana)
    print(args)
    print(kwargs)


exsample_func(100, 'Python-izm', 'パイソンイズム',
              'JP', 'COM', 'US', email='XXXX', city='Tokyo')
