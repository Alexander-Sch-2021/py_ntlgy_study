num = int(input('Номер: '))
n123 = num // 1000
n456 = num % 1000

if n123 // 100 + n123 % 100 // 10 + n123 % 10 == n456 // 100 + n456 % 100 // 10 + n456 % 10:
    print('Счастливый билет')
else:
    print('Несчастливый билет')
