import random


# 0.0 ~ 1.0までのfloat値を取得
print(random.random())
# x ~ y までのfloat値の取得
print(random.uniform(1, 100))
# x ~ y までのint値の取得
print(random.randint(1, 100))
# param内から一つの要素を取得
print(random.choice('1234567890abcdefghij'))

sample_list = ['Python', 'Izm', 'com', 'random', 'sample']
random.shuffle(sample_list)
print(sample_list)
