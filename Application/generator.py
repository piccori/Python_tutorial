def func_sample():
    yield('Hello')
    yield('Good morning')
    yield('Good evening')
    yield('Good night')


# for i in func_sample():
#     print(i)

f = func_sample()
print(next(f))
print(next(f))


gen_sample = (i for i in 'Good Morning Evening Night'.split())

print(gen_sample)
for i in gen_sample:
    print(i)
