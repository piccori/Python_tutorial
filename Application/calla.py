# 指定のオブジェクトが呼び出し可能かを判定する
import sys


def func_test():
    print('function')


class ClassTest():
    pass


str_test = 'str'

print(callable(sys))
print(callable(func_test))
print(callable(ClassTest))
print(callable(str_test))
