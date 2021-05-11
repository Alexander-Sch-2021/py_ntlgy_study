x = input('Введите последовательнось чисел через пробел: ').split()

y = []

for i in x:
    if i not in y:
        y.append(i)

y.sort()

print(*y)
