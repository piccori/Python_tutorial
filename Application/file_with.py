# コンテキストマネジャ
# class ContextManagerText:

#     def __enter__(self):
#         print('__enter__')

#     def __exit__(self, exc_type, exc_value, traceback):
#         print('__exit__')
#         print(exc_type)
#         print(exc_value)
#         print(traceback)
#         return True


# with ContextManagerText():
#     val = int('abc')


# デコレータ
from contextlib import contextmanager


@contextmanager
def context_manager_test():
    print('enter')
    yield
    print('exit')


with context_manager_test():
    print('with')
