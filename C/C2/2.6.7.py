# Скрипт должен конвертировать входные данные в числа:
try:
    i = int(input('Введите число:\t'))

except ValueError as e:
    print('Введено не число!')

else:
    print(f'Вы ввели {i}')

finally:
    print('Выход из программы')
