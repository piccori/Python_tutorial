import datetime


def print_datetime(f):
    def wrapper(*args, **kwargs):
        print(f'開始： {datetime.datetime.now()}')
        f(*args, **kwargs)
        print(f'終了： {datetime.datetime.now()}')
    return wrapper


@print_datetime
def calc(base, height):
    print((base * height) / 2)


calc(5, 4)
