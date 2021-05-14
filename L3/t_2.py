queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]

len_queries = len(queries)

z = {}
for q in queries:
    n = len(q.split(' '))
    if n in z.keys():
        z[n] += 1
    else:
        z[n] = 1

for x in list(sorted(z.items())):
    print(f'Поисковых запросов, содержащих {x[0]} слов(а): {round(x[1] / len_queries * 100, 2)}%')
