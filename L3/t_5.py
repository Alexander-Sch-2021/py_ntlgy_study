# my_list = ['2018-01-01', 'yandex', 'cpc', 100]
# Результат: {'2018-01-01': {'yandex': {'cpc': 100}}}

my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# Результат: {'a': {'b': {'c': {'d': {'e': 'f'}}}}}

for i in range(len(my_list) - 2, -1, -1):
    d = dict()
    if i == len(my_list) - 2:
        d[my_list[i]] = my_list[i + 1]
    else: 
        d[my_list[i]] = dd
    dd = d

print(d)
