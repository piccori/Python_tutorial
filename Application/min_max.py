l_1 = [10, 20, 30, 40, 30, 20, 5]
l_2 = ['A', 'Z', 'K', 'Y', 'S']

# min
print(min(l_1))
print(min(l_2))

# max
print(max(l_1))
print(max(l_2))


# key指定
def key_func(n):
    return int(n)


l: list = [10, 20, 30, 40, 30, 20, 5, '111']
print(min(l, key=key_func))
print(max(l, key=key_func))

l: list = [10, 20, 30, 40, 30, 20, 5, '111']
print(min(l, key=int))
print(max(l, key=int))

print(min(l, key=str))
print(max(l, key=str))


def key_func(n):
    return n[2]


l: list = [(1, 'Python', 100), (2, 'Ruby', 80), (3, 'Perl', 40)]
print(min(l, key=key_func))
print(max(l, key=key_func))


# class
def key_func(n):
    return n.score


class TestClass:

    def __init__(self, code, name, score):
        self.code = code
        self.name = name
        self.score = score

    def __str__(self):
        return f'({self.code}, {self.name}, {self.score})'


l: list = [
    TestClass(1, 'Python', 100),
    TestClass(2, 'Ruby', 80),
    TestClass(3, 'Perl', 40)
    ]
print(min(l, key=key_func))
print(max(l, key=key_func))
