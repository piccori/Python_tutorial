comp_list = [i for i in range(10)]
print(comp_list)

comp_list = [int(i * i) for i in range(10)]
print(comp_list)

comp_dict = {str(i): i * i for i in range(10)}
print(comp_dict)

comp_set = {str(i * i) for i in range(10)}
print(comp_set)

comp_list = [i * j for i in range(1, 10) for j in range(1, 10)]
print(comp_list)

comp_list = [i for i in range(10) if i % 2 == 1]
print(comp_list)
# ジェネレータ
gen = (i for i in range(10))
print(gen)
