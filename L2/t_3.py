x_day = int(input('Введте день: '))

x_month = input('Введите месяц: ')

if x_month == 'январь':
    q_month = 1
elif x_month == 'февраль':
    q_month = 2
elif x_month == 'март':
    q_month = 3
elif x_month == 'апрель':
    q_month = 4
elif x_month == 'май':
    q_month = 5
elif x_month == 'июнь':
    q_month = 6
elif x_month == 'июль':
    q_month = 7
elif x_month == 'август':
    q_month = 8
elif x_month == 'сентябрь':
    q_month = 9
elif x_month == 'октябрь':
    q_month = 10
elif x_month == 'ноябрь':
    q_month = 11
elif x_month == 'декабрь':
    q_month = 12

q_date = q_month * 100 + x_day

if 121 <= q_date <= 219:
    q_zodiac = 'Водолей'
elif 220 <= q_date <= 320:
    q_zodiac = 'Рыбы'
elif 321 <= q_date <= 420:
    q_zodiac = 'Овен'
elif 421 <= q_date <= 521:
    q_zodiac = 'Телец'
elif 522 <= q_date <= 621:
    q_zodiac = 'Близнецы'
elif 622 <= q_date <= 722:
    q_zodiac = 'Рак'
elif 723 <= q_date <= 821:
    q_zodiac = 'Лев'
elif 822 <= q_date <= 923:
    q_zodiac = 'Дева'
elif 924 <= q_date <= 1023:
    q_zodiac = 'Весы'
elif 1024 <= q_date <= 1122:
    q_zodiac = 'Скорпион'
elif 1123 <= q_date <= 1222:
    q_zodiac = 'Стрелец'
elif 1223 <= q_date or q_date <= 120:
    q_zodiac = 'Козерог'

print('Ваш знак зодиака: ', q_zodiac)

# Водолей (21 января — 19 февраля)
# Рыбы (20 февраля — 20 марта)
# Овен (21 марта — 20 апреля)
# Телец (21 апреля — 21 мая)
# Близнецы (22 мая — 21 июня)
# Рак (22 июня — 22 июля)
# Лев (23 июля — 21 августа)
# Дева (22 августа — 23 сентября)
# Весы (24 сентября — 23 октября)
# Скорпион (24 октября — 22 ноября)
# Стрелец (23 ноября — 22 декабря)
# Козерог (23 декабря — 20 января)
