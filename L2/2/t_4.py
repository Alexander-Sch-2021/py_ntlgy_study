countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print('Средняя температура в странах:')
for x in countries_temperature:
    print(x[0], '-', round((sum(x[1]) / len(x[1]) - 32) * 5 / 9, 1))

# print(*countries_temperature)
# C = (F - 32) * 5 / 9