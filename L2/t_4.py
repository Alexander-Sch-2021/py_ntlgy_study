width = 10
length = 205
height = 5

if width < 15 and length < 15 and height < 15:
    print('Коробка №1')
elif length > 200:
    print('Упаковка для лыж')
elif (
      width > 15 or length > 15 or height > 15
     ) and (width < 50 and length < 50 and height < 50):
    print('Коробка №2')
else:
    print('Стандартная коробка №3')
